from flask import Flask, render_template
import yfinance as yf
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stock_graph')
def stock_graph():
    # Fetch data from yfinance for AAPL
    data_aapl = yf.download(tickers='AAPL', period='1d', interval='1m')

    # Create the candlestick chart for AAPL
    fig_aapl = go.Figure(data=[go.Candlestick(
        x=data_aapl.index,
        open=data_aapl['Open'],
        high=data_aapl['High'],
        low=data_aapl['Low'],
        close=data_aapl['Close'],
        name='AAPL'
    )])

    # Add titles and axis labels for AAPL
    fig_aapl.update_layout(
        title='AAPL Stock Price Evolution',
        yaxis_title='Stock Price (USD per Share)'
    )

    # Customize x-axis range selector for AAPL
    fig_aapl.update_xaxes(
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

    # Fetch data from yfinance for NOVO-B.CO
    data_novo = yf.download(tickers='NOVO-B.CO', period='1d', interval='1m')

    # Create the candlestick chart for NOVO-B.CO
    fig_novo = go.Figure(data=[go.Candlestick(
        x=data_novo.index,
        open=data_novo['Open'],
        high=data_novo['High'],
        low=data_novo['Low'],
        close=data_novo['Close'],
        name='NOVO-B.CO'
    )])

    # Add titles and axis labels for NOVO-B.CO
    fig_novo.update_layout(
        title='NOVO-B.CO Stock Price Evolution',
        yaxis_title='Stock Price (DKK per Share)'
    )

    # Customize x-axis range selector for NOVO-B.CO
    fig_novo.update_xaxes(
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

    # Convert the figures to JSON for passing to the template
    graph_json_aapl = fig_aapl.to_json()
    graph_json_novo = fig_novo.to_json()

    return render_template('stock_graph.html', graph_json_aapl=graph_json_aapl, graph_json_novo=graph_json_novo)

if __name__ == '__main__':
    app.run(debug=True)