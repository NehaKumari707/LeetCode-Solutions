-- Last updated: 8/8/2026, 5:21:15 PM
# Write your MySQL query statement below
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;