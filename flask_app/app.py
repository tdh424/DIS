from flask import Flask, render_template
import yfinance as yf
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stock_graph')
def stock_graph():
    # Fetch data from yfinance
    data = yf.download(tickers='AAPL', period='1d', interval='1m')

    # Create the candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='market data'
    )])

    # Add titles and axis labels
    fig.update_layout(
        title='AAPL Stock Price Evolution',
        yaxis_title='Stock Price (USD per Share)'
    )

    # Customize x-axis range selector
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label='15m', step='minute', stepmode='backward'),
                dict(count=45, label='45m', step='minute', stepmode='backward'),
                dict(count=1, label='HTD', step='hour', stepmode='todate'),
                dict(count=3, label='3h', step='hour', stepmode='backward'),
                dict(step='all')
            ])
        )
    )

    # Convert the figure to JSON for passing to the template
    graph_json = fig.to_json()

    return render_template('stock_graph.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)