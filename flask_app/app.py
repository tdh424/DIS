from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/stonkviewer'
db = SQLAlchemy(app)

class Stock(db.Model):
    __tablename__ = 'stocks'
    Date = db.Column(db.DateTime, primary_key=True)
    Open = db.Column(db.Float)
    High = db.Column(db.Float)
    Low = db.Column(db.Float)
    Close = db.Column(db.Float)
    AdjClose = db.Column(db.Float)
    Volume = db.Column(db.Integer)
    Ticker = db.Column(db.String(10))

@app.route('/')
def home():
    stocks = Stock.query.all()
    return render_template('index.html', stocks=stocks)

if __name__ == '__main__':
    app.run(debug=True)
