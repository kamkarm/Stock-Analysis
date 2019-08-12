"""
Returns Apple's, Google's, and Facebook's stocks from 2019 in Json format

Data is acquired through the Financial Modeling Prep API
"""

import requests

def fetch_2019_data():

	#Connect to API and get historical data from January 1st 2019 - current date
	url = 'https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,FB'
	param = {'from': '2019-01-01'}
	resp = requests.get(url = url, params = param)
	data = None
	#Make sure there is a proper connection to API
	if resp.ok:
		data = resp.json()['historicalStockList']
	else:
		print('Connection to API Failed')
	return data