"""
SQL query functions to create stocks table and populate it
"""

import psycopg2

def create_table(cur):

	""" 
	Create table stocks if it doesn't already exist (create_table)

	Input: Psycopg2 cursor
	"""

	cur.execute("""
		CREATE TABLE IF NOT EXISTS stocks (
		symbol              TEXT,
	    open_day            DATE,
		opened              REAL,
		high                REAL,
		low                 REAL,
		closed              REAL,
		volume              BIGINT,
		PRIMARY KEY (symbol, open_day)
							)
	""")

def insert(data, cur):

	""" 
	Insert data in Json format into the stocks table (insert)

	Inputs:

	data: Json from fetch_data.fetch_2019_data()
	cur: Psycopg2 cursor
	"""

	#For every symbol (AAPL, GOOGL, FB)
	for item in data:
		symbol = item['symbol']
		rows = item['historical']
		#For every row corresponding to a day
		for row in rows:
			my_data = [symbol] + [row[field] for field in row]
			#Only insert first seven elements
			cur.execute("""
				INSERT INTO stocks VALUES 
		    	(%s, %s, %s, %s, %s, %s, %s)""", tuple(my_data[:7]))

def percent_change_column(cur):

	"""
	Add and populate column percent_change to stock table

	This function will first add a column to the stocks table,
	then replace default (NULL) values with values calculated
	from table.

	Percent_change is caculated by:
	(row closing value) - (previous day's closing value) / row closing value * 100

	Input: Psycopg2 cursor
	"""
	
	cur.execute("""
		ALTER TABLE stocks 
		ADD COLUMN percent_change REAL
				""")

	cur.execute("""
		UPDATE stocks
		SET percent_change = sub.change
		FROM (
			SELECT 
				symbol, 
		   		open_day, 
		   		(closed - LAG(closed, 1) OVER (
											PARTITION BY symbol 
											ORDER BY open_day
											)) / closed * 100 AS change
			FROM stocks) AS sub
		WHERE 
			stocks.symbol = sub.symbol 
			AND stocks.open_day = sub.open_day
				""")
