-- Last updated: 8/8/2026, 5:22:27 PM
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee r
ON e.id = r.managerId
GROUP BY e.id, e.name
HAVING COUNT(r.id) >= 5;
