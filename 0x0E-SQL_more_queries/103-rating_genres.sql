-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Eaach record display: tv_genres.name - rating sum
-- Sorted in descending order by their rating
-- Use only one SELECT statement
SELECT name, SUM(rate) AS total_rating
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tsg.genres_id = tg.id

       INNER JOIN tv_show_genres AS tsg
       ON tsg.show_id = tg.show_id
 GROUP BY name
 ORDER BY total_rating DESC;
