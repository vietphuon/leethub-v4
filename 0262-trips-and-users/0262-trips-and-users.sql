# Write your MySQL query statement below
WITH cte AS (SELECT t.*
FROM Trips t
LEFT JOIN Users u1
ON t.client_id = u1.users_id
LEFT JOIN Users u2
ON t.driver_id = u2.users_id
WHERE u1.banned = 'No'
AND u2.banned = 'No'
)
SELECT request_at AS Day, ROUND(SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) / COUNT(DISTINCT id), 2) AS 'Cancellation Rate'
FROM cte
WHERE request_at >= '2013-10-01' AND request_at <= '2013-10-03'
GROUP BY request_at 
