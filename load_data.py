"""
Data dump into PostgreSQL table

This script will load data from Financial Modeling Prep API from 1/02/2019 
to current date and dump the data into an existing AWS PostgreSQL table. 
"""

import requests
import psycopg2
import os

if __name__ == '__main__':
	#connect to API and get historical data from January 1st 2019 - current date
	URL = 'https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,FB'
	PARAM = {'from': '2019-01-01'}
	resp = requests.get(url = URL, params = PARAM)

	#Make sure there is a proper connection to API
	if resp.ok:
		data = resp.json()['historicalStockList']

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
				con.commit()
			except psycopg2.DatabaseError as error:
				print(error)
				print('data was not loaded')
			finally:
				if con is not None:
					con.close()
	else:
		print('Connection to API Error')
