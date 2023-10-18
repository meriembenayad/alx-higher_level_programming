-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record display: tv_shows.title
-- Sorted in ascending order by the show title
-- Use only one SELECT statement
SELECT title FROM tv_shows
JOIN tv_show_genres ON id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
