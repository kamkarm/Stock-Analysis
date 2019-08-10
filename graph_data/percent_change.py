"""
Graph the percent change per day for each stock

Percent_change calculation by:
(row closing value) - (previous day's closing value) / row closing value * 100
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
		cur.execute("""
			SELECT 
				symbol, 
				percent_change
			FROM stocks
					""")
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
			plt.ylabel('Percent Change')
			plt.title('Percent Change per Day for ' + stock)
			plt.show()
	finally:
		if con is not None:
			con.close()