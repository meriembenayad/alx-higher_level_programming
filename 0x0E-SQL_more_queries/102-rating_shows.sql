-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_shows.title - rating sum
-- Sorted in descending order by the rating
-- Use only one SELECT statement
SELECT title, SUM(rating) AS total_rating
FROM tv_shows As ts
    INNER JOIN tv_show_rating As tr
    ON ts.id = tr.show_id
GROUP BY title
ORDER BY total_rating DESC;
