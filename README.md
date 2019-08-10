# Stock-Analysis

Analysis of stocks (Apple, Google, Facebook) from 1/02/2019

_Written by Michael Kamkar_

In this project, I:

1. Pulled historical data from a financial stocks API and loaded the data into an AWS RDS PostgreSQL table
2. Analayzed the data using window functions and plots
3. Scheduled an AWS lambda cron function to add latest stock prices daily

Data was acquired the Financial Modeling Prep API through:

https://financialmodelingprep.com/developer/docs/#Stock-Price

Note: The Json file in the data folder only contains data up till 8/09/2019

