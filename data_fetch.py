from apscheduler.schedulers.background import BackgroundScheduler
import yfinance as yf
from sqlalchemy import create_engine
from datetime import datetime

# Create a connection to your PostgreSQL database
engine = create_engine('postgresql://@localhost/emil')

def fetch_and_store(ticker="AAPL"):
    # Fetch data from yfinance
    data = yf.download(ticker, period="1d", interval="1m")
    
    # Rename the columns to match your database
    data.rename(columns={"Adj Close": "Adj_Close"}, inplace=True)
    
    # Add a datetime column with the current timestamp
    data['Datetime'] = datetime.now()
    
    # Store the data in the "stocks" table
    data.to_sql('stocks', con=engine, if_exists='append', index=False)

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_and_store, trigger="interval", seconds=10)
scheduler.start()

# To keep the script running
while True:
    pass
