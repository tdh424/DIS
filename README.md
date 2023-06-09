# DIS
DIS Project STONKVIEWER

To run our project you firstly have to install some packages:
pip install

Furthermore in your query console insert the code provided in the scema.sql to create the correct table to be filled with data and extracted into the web app.

In the file app.py you have to connect your postgreSQL using psycopg2.

When the SQL console has been deployed the simply locate the following file and the write "flask run":
app.py

To access the web app go to your desired web app and use the url: http://127.0.0.1/

When met with the log in page a user has been created.
Username: DIS
Password: 123

From here you will be redirected to the stock_graph page, and you can see what we have implemented.

The current fuctions that does work:
Login
Logout
Stock graphs

What is not done:
The option to buy/sell in the end of the page is not currently fuctional, even though the nessesary calculations is done, it lags a complete solution.
A counter for the total amount of units and amount of each stock.
