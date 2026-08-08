-- Last updated: 8/8/2026, 5:22:09 PM
# Write your MySQL query statement below
SELECT id, visit_date, people
FROM (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
) t
WHERE grp IN (
    SELECT grp
    FROM (
        SELECT id - ROW_NUMBER() OVER (ORDER BY id) AS grp
        FROM Stadium
        WHERE people >= 100
    ) x
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;