-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Eaach record display: tv_genres.name - rating sum
-- Sorted in descending order by their rating
-- Use only one SELECT statement
SELECT tv_genres.name, SUM(rating) AS total_rating
FROM hbtn_0d_tvshows_rate
INNER JOIN tv_genres ON hbtn_0d_tvshows_rate.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY total_rating DESC;
