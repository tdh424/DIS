from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf
import plotly.graph_objects as go
import psycopg2
import pandas as pd

app = Flask(__name__)

# Connect to your PostgreSQL DB
conn = psycopg2.connect(
    dbname="emil",
    user="",
    password="",
    host="127.0.0.1"
)
cur = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the entered username and password from the login form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'DIS' and password == '123':
            return redirect(url_for('stock_graph'))

    return render_template('home.html')

@app.route('/stock_graph')
def stock_graph():
    # Fetch data from yfinance for AAPL
    data_aapl = yf.download(tickers='AAPL', period='1d', interval='1m')

    # Insert or update AAPL data into database
    data_aapl.reset_index(inplace=True)
    data_aapl_columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data_aapl_values = data_aapl[data_aapl_columns].values.tolist()
    insert_query_aapl = """
        INSERT INTO aapl_data (Datetime, Open, High, Low, Close, "Adj Close", Volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.executemany(insert_query_aapl, data_aapl_values)
    conn.commit()

    # Fetch AAPL data from database
    aapl_query = "SELECT * FROM aapl_data;"
    cur.execute(aapl_query)
    aapl_rows = cur.fetchall()
    data_aapl = pd.DataFrame(aapl_rows, columns=data_aapl_columns)

    # Create the candlestick chart for AAPL
    fig_aapl = go.Figure(data=[go.Candlestick(
        x=data_aapl['Datetime'],
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

    # Insert or update NOVO data into database
    data_novo.reset_index(inplace=True)
    data_novo_columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data_novo_values = data_novo[data_novo_columns].values.tolist()
    insert_query_novo = """
        INSERT INTO novo_data (Datetime, Open, High, Low, Close, "Adj Close", Volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.executemany(insert_query_novo, data_novo_values)
    conn.commit()

    # Fetch NOVO data from database
    novo_query = "SELECT * FROM novo_data;"
    cur.execute(novo_query)
    novo_rows = cur.fetchall()
    data_novo = pd.DataFrame(novo_rows, columns=data_novo_columns)

    # Create the candlestick chart for NOVO-B.CO
    fig_novo = go.Figure(data=[go.Candlestick(
        x=data_novo['Datetime'],
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

    graph_json_aapl = fig_aapl.to_json()
    graph_json_novo = fig_novo.to_json()

    return render_template('stock_graph.html', graph_json_aapl=graph_json_aapl, graph_json_novo=graph_json_novo)

if __name__ == '__main__':
    app.run(debug=True)