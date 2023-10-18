-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_shows.title - rating sum
-- Sorted in descending order by the rating
-- Use only one SELECT statement
SELECT ts.title, SUM(tr.rate) AS total_rating
FROM tv_shows ts, tv_show_ratings tr
WHERE ts.id = tr.show_id
GROUP BY ts.title
ORDER BY total_rating DESC;
