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
CREATE INDEX ix_stocks_Datetime ON stocks("Datetime");