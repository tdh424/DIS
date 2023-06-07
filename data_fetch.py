from apscheduler.schedulers.background import BackgroundScheduler
import yfinance as yf
from sqlalchemy import create_engine

# Create a connection to your PostgreSQL database
engine = create_engine('postgresql://@localhost/stonkviewer')

def fetch_and_store(ticker="AAPL"):
    # Fetch data from yfinance
    data = yf.download(ticker, period="1d", interval="1m")
    
    # Save the data to your PostgreSQL database
    data.to_sql('stocks', con=engine, if_exists='append')

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_and_store, trigger="interval", seconds=60)
scheduler.start()

# To keep the script running
while True:
    pass