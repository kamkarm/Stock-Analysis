"""
Create stocks table
"""

import psycopg2
import sys
sys.path.append('../')
import db

if __name__ == "__main__":
	con = db.connect()
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
	finally:
		if con is not None:
			con.close()