CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    adj_close FLOAT,
    volume INTEGER
);
