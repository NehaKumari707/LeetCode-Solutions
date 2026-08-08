-- Last updated: 8/8/2026, 5:22:06 PM
# Write your MySQL query statement below
SELECT 
    x,
    y,
    z,
    CASE 
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;