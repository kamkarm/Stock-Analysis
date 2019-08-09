-- create new column for percent_change
ALTER TABLE stocks 
ADD COLUMN percent_change REAL;

-- percent_change will be the percent difference between yesterdays and todays
-- closing stock price
UPDATE stocks
SET percent_change = sub.change
FROM (
	SELECT 
		symbol, 
   		open_day, 
   		(closed - LAG(closed, 1) OVER (
									PARTITION BY symbol 
									ORDER BY open_day
									)) / closed * 100 AS change
	FROM stocks) AS sub
WHERE 
	stocks.symbol = sub.symbol 
	AND stocks.open_day = sub.open_day