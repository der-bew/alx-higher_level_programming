-- Displays the average temperature by city ordered by temperature (desc)
SELECT city, ROUND(AVG(value) AS avg_temp, 4)
   FROM temperatures
   GROUP BY city
   ORDER BY avg_temp;
