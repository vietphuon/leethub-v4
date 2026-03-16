# Write your MySQL query statement below
WITH cte AS (SELECT l1.id, l1.num, l2.num as nnum
FROM Logs l1
CROSS JOIN Logs l2
WHERE l1.id + 1 = l2.id
)
SELECT DISTINCT c.num AS ConsecutiveNums
FROM cte c
CROSS JOIN Logs l
WHERE c.id + 2 = l.id AND c.num = c.nnum AND c.nnum = l.num