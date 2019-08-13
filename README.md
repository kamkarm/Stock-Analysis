# Stock-Analysis

Analysis of stocks (Apple, Google, Facebook) from 1/02/2019

_Written by Michael Kamkar_

In this project, I:

1. Pulled historical data from a financial stocks API and loaded the data into an AWS RDS PostgreSQL table
2. Analayzed the data using window functions and plots
3. Scheduled an AWS lambda cron function to add latest stock prices daily to database

load_data in the initialize_table folder will create and populate a table called stocks.
Each script in the graph_data folder will plot each of the graphs (graphs located in graphs folder).
aws_lambda folder has the deployment_package zip file to run a scheduled lambda cron function and screenshots of my lambda function on AWS.

Data was acquired through the Financial Modeling Prep API:

https://financialmodelingprep.com/developer/docs/#Stock-Price

Note: The Json file in the data folder only contains data up till 8/09/2019

