import psycopg2
import os

def connect():
	"""
	This function should connect to my AWS rds database and return the connection.
	If connection fails, message will be displayed, and None with be returned
	"""
	
	dbname = 'postgres'
	user = 'postgres'
	host = os.environ.get('aws_host')
	port = 5432
	pw = os.environ.get('aws_pw')
	con = None	
	try:
		con = psycopg2.connect(dbname = dbname, 
							   user = user, 
							   host = host, 
							   port = port,
							   password = pw)
	except psycopg2.OperationalError as error:
		print(error)
	finally:
		return con