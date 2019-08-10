"""
Data dump into PostgreSQL table

This script will load data from Financial Modeling Prep API from 1/02/2019 
to current date and dump the data into an existing AWS PostgreSQL table. 
"""

import requests
import psycopg2
import sys
sys.path.append('../')
import db

if __name__ == '__main__':
	con = db.connect()
	cur = con.cursor()
	#Check if data has already been loading to db
	cur.execute('SELECT EXISTS (SELECT 1 FROM stocks)')
	exists = cur.fetchone()[0]
	if not exists:
		#Connect to API and get historical data from January 1st 2019 - current date
		url = 'https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,FB'
		param = {'from': '2019-01-01'}
		resp = requests.get(url = url, params = param)
		#Make sure there is a proper connection to API
		if resp.ok:
			data = resp.json()['historicalStockList']
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
			finally:
				if con is not None:
					con.close()
		else:
			print('Connection to API Failed')
	else:
		print('Table already initialized')