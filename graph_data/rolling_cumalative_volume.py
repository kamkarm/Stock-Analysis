"""
Graph the rolling cumulative volume for each stock
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
		cur.execute(open('sql_queries/rolling_cumulative_volume.sql').read())
	except psycopg2.DatabaseError as error:
		print(error)
	else:
		result = cur.fetchall()
		data = {'AAPL' : [], 'FB': [], 'GOOG': []}

		for symbol, val in result:
			data[symbol].append(val)

		xTickMarks = [i for i in range(len(data['AAPL']))]

		for stock, vals in data.items():
			plt.plot(xTickMarks,vals)
			plt.xlabel('Days Since January 2nd 2019')
			plt.ylabel('Rolling Cumulative Volume')
			plt.title('Rolling Cumulative Volume Since January 2nd 2019 for ' + stock)
			plt.show()

	finally:
		if con is not None:
			con.close()