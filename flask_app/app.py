from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/emil'
db = SQLAlchemy(app)


class Stock(db.Model):
    __tablename__ = 'stocks'
    datetime = db.Column(db.DateTime, primary_key=True, name="Datetime")
    open = db.Column(db.Float, name="Open")
    high = db.Column(db.Float, name="High")
    low = db.Column(db.Float, name="Low")
    close = db.Column(db.Float, name="Close")
    adj_close = db.Column(db.Float, name="Adj_Close")
    volume = db.Column(db.Integer, name="Volume")
    ticker = db.Column(db.String(10), name="Ticker")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stock_graph')
def stock_graph():
    stocks = Stock.query.all()

    return render_template('stock_graph.html', stocks=stocks)


if __name__ == '__main__':
    app.run(debug=True)