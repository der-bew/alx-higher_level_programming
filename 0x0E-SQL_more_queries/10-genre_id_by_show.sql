-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
   -- Each record should display: tv_shows.title - tv_show_genres.genre_id
   -- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT ts.title, tsg.genre_id
   FROM tv_shows AS ts
   INNER JOIN tv_show_genres AS tsg ON tsg.tv_show_genres_ibfk_1 = ts.id
   ORDER BY ts.title, tsg.genre_id;
