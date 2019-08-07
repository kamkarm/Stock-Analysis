CREATE TABLE stocks (
	symbol              TEXT,
    open_day            DATE,
	opened              REAL,
	high                REAL,
	low                 REAL,
	closed              REAL,
	volume              BIGINT,
	PRIMARY KEY (symbol, open_day)
	)