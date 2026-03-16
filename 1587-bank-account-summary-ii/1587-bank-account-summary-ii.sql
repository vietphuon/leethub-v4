# Write your MySQL query statement below
SELECT name, SUM(amount) as balance
FROM Users as u
JOIN Transactions as t
ON u.account = t.account
GROUP BY name
HAVING SUM(amount) > 10000