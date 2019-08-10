-- contains the rolling cumulative volume for each stock
SELECT 
	symbol,
	SUM(volume) OVER (
					PARTITION BY symbol 
					ORDER BY open_day
					) AS total_trades
FROM stocks