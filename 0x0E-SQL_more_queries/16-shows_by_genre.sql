-- Lists all shows, and all genres linked to that show
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record display: tv_shows.title - tv_genres.name
-- Sorted in ascending order by the show title and genre name
-- Use only one SELECT statement
SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name ASC;
