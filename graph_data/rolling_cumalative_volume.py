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
		cur.execute("""
			SELECT 
				symbol,
				SUM(volume) OVER (
								PARTITION BY symbol 
								ORDER BY open_day
								) AS total_trades
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
			plt.ylabel('Rolling Cumulative Volume')
			plt.title('Rolling Cumulative Volume Since January 2nd 2019 for ' + stock)
			plt.show()

	finally:
		if con is not None:
			con.close()