-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, ROUND(AVG(value) AS avg_temp, 4)
   FROM temperatures
   WHERE month BETWEEN 7 AND 8
   GROUP BY city
   ORDER BY avg_temp DESC
   LIMIT 3;
