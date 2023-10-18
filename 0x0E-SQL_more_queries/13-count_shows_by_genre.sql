-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Sorted in descending order by the number of shows linked
-- Use only one SELECT statement
SELECT name AS genre, count(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
