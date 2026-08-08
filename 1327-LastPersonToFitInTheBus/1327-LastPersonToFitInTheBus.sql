-- Last updated: 8/8/2026, 5:21:34 PM
# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT 
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) t
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;