-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_shows.title - rating sum
-- Sorted in descending order by the rating
-- Use only one SELECT statement
SELECT tvs.title, IFNULL(SUM(tvsr.rate), 0) AS total_rating
FROM tv_shows AS tvs
LEFT JOIN tv_show_ratings AS tvsr ON tvs.id =  tvsr.show_id
GROUP BY tvs.title
ORDER BY total_rating DESC;

