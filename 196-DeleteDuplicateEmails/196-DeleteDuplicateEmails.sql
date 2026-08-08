-- Last updated: 8/8/2026, 5:22:34 PM
# Write your MySQL query statement below
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email AND p1.id > p2.id;