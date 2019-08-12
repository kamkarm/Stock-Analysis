"""
Data dump into PostgreSQL table

This script will load data from Financial Modeling Prep API from 1/02/2019 
to current date and dump the data into an existing AWS PostgreSQL table. 
"""

from fetch_data import load_2019_data
from insert_data import insert

if __name__ == '__main__':
	data = load_2019_data()
	if data:
		insert(data)