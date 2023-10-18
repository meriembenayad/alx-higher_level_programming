-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record display: tv_shows.title
-- Sorted in ascending order by the show title
-- Use a maximum of two SELECT statement
SELECT tv_shows.title FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name != 'Comedy' OR tv_genres.name IS NULL
ORDER BY tv_shows.title ASC;

