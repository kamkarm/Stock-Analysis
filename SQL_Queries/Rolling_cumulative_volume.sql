-- contains the rolling cumulative volume for each stock
SELECT symbol, 
	   open_day,
	   volume,
	   SUM(volume) OVER (
				PARTITION BY symbol 
				ORDER BY open_day
				) AS total_trades
FROM stocks