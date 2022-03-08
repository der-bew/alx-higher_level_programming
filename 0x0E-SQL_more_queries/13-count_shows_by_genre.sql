-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
   -- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
   -- First column must be called genre
   -- Second column must be called number_of_shows
   -- Don’t display a genre that doesn’t have any shows linked
   -- Results must be sorted in descending order by the number of shows linked
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT tg.name AS genre, COUNT(*) AS number_of_shows
   FROM tv_genres AS tg
   INNER JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
   GROUP BY tsg.genre_id
   ORDER BY number_of_shows DESC;
