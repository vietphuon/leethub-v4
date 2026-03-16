# Write your MySQL query statement below

WITH cte AS (SELECT *, (id - DENSE_RANK() OVER(ORDER BY id ASC)) AS diff
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people 
FROM cte
WHERE diff IN (
    SELECT diff
    FROM cte
    GROUP BY diff
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date ASC