-- Last updated: 8/8/2026, 5:20:57 PM
# Write your MySQL query statement below
SELECT 
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;