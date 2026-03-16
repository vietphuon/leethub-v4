# Write your MySQL query statement below
WITH cte AS (
SELECT o.order_id, o.order_date, o.buyer_id, u.join_date, COUNT(DISTINCT o.order_id) AS orders_in_2019
FROM Orders o
LEFT JOIN Users u
ON o.buyer_id = u.user_id
WHERE o.order_date LIKE '2019%'
GROUP BY o.buyer_id
)
SELECT u.user_id AS buyer_id, u.join_date, CASE 
    WHEN ISNULL(c.orders_in_2019) THEN 0
    ELSE c.orders_in_2019
    END
AS orders_in_2019
FROM Users u
LEFT JOIN cte c
ON u.user_id = c.buyer_id