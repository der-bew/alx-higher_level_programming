-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
   -- If a show doesn’t have a genre, display NULL in the genre column
   -- Each record should display: tv_shows.title - tv_genres.name
   -- Results must be sorted in ascending order by the show title and genre name
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT ts.title, tg.name
   FROM tv_shows AS ts
   LEFT JOIN tv_show_genres AS tsg
   ON tsg.show_id = ts.id
   INNER JOIN tv_genres AS tg
   ON tg.id = tsg.genre_id;
   ORDER BY 1, 2;
