"""
Add and populate column percent_change to stock table

This script will first add a column to the stocks table,
then replace default (NULL) values with values calculated
from table.

Percent_change is caculated by:
(row closing value) - (previous day's closing value) / row closing value * 100
"""

import psycopg2
import sys
sys.path.append('../')
import db


if __name__ == "__main__":
	con = db.connect()
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
	finally:
		if con is not None:
			con.close()