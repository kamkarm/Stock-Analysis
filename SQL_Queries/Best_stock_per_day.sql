-- Returns stock with largest percent change of the day if > 0
SELECT 
	symbol, 
	open_day, 
    percent_change
FROM (
	SELECT 
		symbol,
  		open_day,
  		percent_change,
  		RANK() OVER (
	  		PARTITION BY open_day 
	  		ORDER by percent_change
	  		) AS rank
  	FROM stocks
  	WHERE percent_change > 0) AS sub
WHERE rank = 1