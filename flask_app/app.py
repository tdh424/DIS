from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/stonkviewer'
db = SQLAlchemy(app)

class Stock(db.Model):
    __tablename__ = 'stocks'
    Datetime = db.Column(db.DateTime, primary_key=True)
    Open = db.Column(db.Float)
    High = db.Column(db.Float)
    Low = db.Column(db.Float)
    Close = db.Column(db.Float)
    Adj_Close = db.Column(db.Float) 
    Volume = db.Column(db.Integer)
    ticker = db.Column(db.String(10)) 

@app.route('/')
def home():
    # Retrieve the stock data from the database
    stocks = Stock.query.all()

    # Print the column names
    for stock in stocks:
        print(stock.__dict__.keys())  # Print the column names

    return render_template('home.html', stocks=stocks)

if __name__ == '__main__':
    app.run(debug=True)
