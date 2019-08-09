"""
Graph the percent change per day for each stock

Percent_change calculation by:
(row closing value) - (previous day's closing value) / row closing value * 100
"""

import psycopg2
import os
import matplotlib.pyplot as plt

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