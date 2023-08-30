-- list records with a name in descending order wrt score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
