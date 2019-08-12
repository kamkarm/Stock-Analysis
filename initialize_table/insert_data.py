"""
Inserts data into AWS rds database

Input: Json data from Financial Modeling Prep API
"""

import psycopg2
import sys
sys.path.append('../')
import db

def insert(data):

	con = db.connect()
	cur = con.cursor()
	#Check if data has already been loading to db
	cur.execute('SELECT EXISTS (SELECT 1 FROM stocks)')
	table = cur.fetchone()[0]
	if not table:
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
		print('Table already initialized')