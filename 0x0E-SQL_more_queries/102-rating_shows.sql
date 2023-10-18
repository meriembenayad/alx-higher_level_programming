-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_shows.title - rating sum
-- Sorted in descending order by the rating
-- Use only one SELECT statement
SELECT tv_shows.title, SUM(rating) AS total_rating
FROM hbtn_0d_tvshows_rate
INNER JOIN tv_shows ON hbtn_0d_tvshows_rate.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY total_rating DESC;
