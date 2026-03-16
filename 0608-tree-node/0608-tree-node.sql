# Write your MySQL query statement below
-- SELECT id, CASE WHEN ISNULL(p_id) THEN 'Root'
-- WHEN THEN
-- ELSE
-- END AS type
-- FROM Tree
WITH cte2 AS (
WITH cte AS (
SELECT p_id as id ,GROUP_CONCAT(id SEPARATOR ',') AS c_id
FROM Tree
GROUP BY p_id
)
SELECT t.*, c_id
FROM Tree t
LEFT JOIN cte c
ON t.id = c.id
)
SELECT id, CASE WHEN ISNULL(p_id) THEN 'Root'
    WHEN ISNULL(c_id) THEN 'Leaf'
    ELSE 'Inner'
END AS type
FROM cte2