-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record display: tv_genres.name
-- Sorted in ascending order by the genre name
-- Use only one SELECT statement
SELECT name FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
