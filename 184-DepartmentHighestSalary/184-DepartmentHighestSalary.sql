-- Last updated: 8/8/2026, 5:22:40 PM
# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY departmentId 
               ORDER BY salary DESC
           ) AS rnk
    FROM Employee
) e
JOIN Department d 
    ON e.departmentId = d.id
WHERE e.rnk = 1;