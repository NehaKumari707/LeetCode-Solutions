-- Last updated: 8/8/2026, 5:20:40 PM
# Write your MySQL query statement below
WITH RECURSIVE hierarchy AS (
    -- Step 1: Build levels
    SELECT 
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT 
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    FROM Employees e
    JOIN hierarchy h 
        ON e.manager_id = h.employee_id
),

subtree AS (
    -- Step 2: Build all ancestor-child relationships
    SELECT 
        employee_id AS root_id,
        employee_id AS sub_id,
        salary
    FROM Employees

    UNION ALL

    SELECT 
        s.root_id,
        e.employee_id,
        e.salary
    FROM subtree s
    JOIN Employees e 
        ON e.manager_id = s.sub_id
)

-- Step 3: Aggregate results
SELECT 
    h.employee_id,
    h.employee_name,
    h.level,
    COUNT(s.sub_id) - 1 AS team_size,
    SUM(s.salary) AS budget
FROM hierarchy h
JOIN subtree s 
    ON h.employee_id = s.root_id
GROUP BY h.employee_id, h.employee_name, h.level
ORDER BY 
    h.level ASC,
    budget DESC,
    h.employee_name ASC;