-- Last updated: 8/8/2026, 5:22:24 PM
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;