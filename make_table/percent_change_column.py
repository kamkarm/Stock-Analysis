"""
Add and populate column percent_change to stock table

This script will first add a column to the stocks table,
then replace default (NULL) values with values calculated
from table.

Percent_change is caculated by:
(row closing value) - (previous day's closing value) / row closing value * 100
"""

import psycopg2
import os


if __name__ == "__main__":
	dbname = 'postgres'
	user = 'postgres'
	host = os.environ.get('aws_host')
	port = 5432
	pw = os.environ.get('aws_pw')
	try:
		con = psycopg2.connect(dbname = dbname, 
							   user = user, 
							   host = host, 
							   port = port,
							   password = pw)
	except:
		print('Connection to Database Error')
	else:
		cur = con.cursor()
		try:
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
			con.commit()
		except psycopg2.DatabaseError as error:
			print(error)
			print('percent_change was not created')
		finally:
			if con is not None:
				con.close()