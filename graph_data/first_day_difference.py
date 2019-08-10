"""
Create a line graph of how the stock value compares to it's value on 1/02/2019 
for each stock.

For each stock, the query will find the difference between the stock's
value at day X and 1/02/2019 

Query is then plotted on as a bar graph on matplotlib 
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
		cur.execute(open('sql_queries/first_day_difference.sql').read())
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
			plt.ylabel('Current Day and January 2nd 2019 Stock Price Difference')
			plt.title('Stock Growth from January 2nd 2019 per Day for ' + stock)
			plt.show()			
	finally:
		if con is not None:
			con.close()