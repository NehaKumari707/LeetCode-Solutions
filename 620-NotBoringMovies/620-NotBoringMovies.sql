-- Last updated: 8/8/2026, 5:21:59 PM
# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
