"""
Create stocks table
"""

import psycopg2
import os

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
				CREATE TABLE stocks (
				symbol              TEXT,
			    open_day            DATE,
				opened              REAL,
				high                REAL,
				low                 REAL,
				closed              REAL,
				volume              BIGINT,
				PRIMARY KEY (symbol, open_day)
									)
			""")
			con.commit()
		except psycopg2.DatabaseError as error:
			print(error)
			print('Table was not created')
		finally:
			if con is not None:
				con.close()