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
					count(*)
				FROM (
					SELECT 
						symbol,
				  		open_day,
				  		percent_change,
				  		RANK() OVER (
					  		PARTITION BY open_day 
					  		ORDER by percent_change
					  		) AS rank
				  	FROM stocks
				  	WHERE percent_change > 0) AS sub
				WHERE rank = 1
				GROUP BY symbol
							""")
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