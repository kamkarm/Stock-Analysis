"""
Data dump into PostgreSQL table

This script will load data from Financial Modeling Prep API from 1/02/2019 
to current date, dump the data into an existing AWS PostgreSQL table, and
add a percent_change column (calculated from the data itself).
"""

from psycopg2 import DatabaseError
import sys
sys.path.append('../')
import db
from fetch_data import fetch_2019_data
import insert_data

if __name__ == '__main__':
	try:
		con = db.connect()
		cur = con.cursor()
		#Create table if not exists
		insert_data.create_table(cur)
	except DatabaseError as error:
		print(error)
	else:
		#Check if there are already rows in table
		#If there are already rows, do nothing
		cur.execute('SELECT EXISTS (SELECT 1 FROM stocks)')
		rows = cur.fetchone()[0]
		if not rows:
			#Fetch data from API
			data = fetch_2019_data()
			#If data was retreived
			if data:
				try:
					#Dump data into table and add percent_change column
					#to the table
					insert_data.insert(data, cur)
					insert_data.percent_change_column(cur)
					print('Data inserted to table')
					con.commit()
				except DatabaseError as error:
					print(error)
					print('There were no commits')
		else:
			print('Table already initialized')
	finally:
		if con is not None:
			con.close()