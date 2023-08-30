-- select number of records with the same score in table

SELECT score, COUNT(score) AS "number" GROUP BY score ORDER BY score DESC
