-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record display: tv_shows.title - tv_show_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Use only one SELECT statement
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id ASC;
