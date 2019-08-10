/* contains column with difference between row's closing stock price
   and the closing stock price at the beginning of the year */
SELECT 
	symbol, 
	closed - FIRST_VALUE (closed) OVER (
   									PARTITION BY symbol 
	   								ORDER BY open_day
	   									) AS difference
FROM stocks