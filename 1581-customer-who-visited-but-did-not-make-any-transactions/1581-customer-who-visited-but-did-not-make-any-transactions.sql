# Write your MySQL query statement below
SELECT v.customer_id, COUNT(DISTINCT v.visit_id) as count_no_trans
FROM Visits as v
LEFT JOIN Transactions as t
ON v.visit_id = t.visit_id
WHERE ISNULL(t.transaction_id)
GROUP BY v.customer_id
-- HAVING COUNT(ISNULL(transaction_id)) > 0