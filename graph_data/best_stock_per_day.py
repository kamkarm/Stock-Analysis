"""
Create bar graph counting how many times a stock had the largest percent change
per day

This script will query the database by:
1.) Ranking each stock's percent_change per day
2.) Selecting stocks with the largest percent_change (rank = 1)
3.) Counting how many times a stock's percent_change was the largest

Query is then plotted as a bar graph on matplotlib 
"""

import psycopg2
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import db

if __name__ == "__main__":
	con = db.connect()
	cur = con.cursor()
	try:
		cur.execute(open('sql_queries/best_stock_per_day.sql').read())
	except psycopg2.DatabaseError as error:
		print(error)
	else:
		result = cur.fetchall()
		
		data = []
		xTickMarks = []

		for row in result:
			data.append(row[1])
			xTickMarks.append(row[0])

		plt.bar(xTickMarks,data)
		plt.xlabel('Stock Symbol')
		plt.ylabel('Largest Growth Count')
		plt.title('Cumulative Count of Stock with Largest Growth per Day')
		plt.show()
	finally:
		if con is not None:
			con.close()