\c stonkviewer
DROP TABLE IF EXISTS stocks;

CREATE TABLE stocks (
    "Datetime" timestamp with time zone,
    "Open" double precision,
    "High" double precision,
    "Low" double precision,
    "Close" double precision,
    "Adj_Close" double precision,
    "Volume" bigint,
    "Ticker" varchar(10)
);

CREATE TABLE IF NOT EXISTS aapl_data (
    Datetime TIMESTAMP,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    "Adj Close" FLOAT,
    Volume FLOAT
    );

CREATE TABLE IF NOT EXISTS novo_data (
    Datetime TIMESTAMP,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    "Adj Close" FLOAT,
    Volume FLOAT
    );

CREATE INDEX ix_stocks_Datetime ON stocks("Datetime");