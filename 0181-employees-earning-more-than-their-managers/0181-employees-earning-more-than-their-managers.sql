# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee as e
INNER JOIN Employee as m
ON e.managerID = m.id
-- GROUP BY e.id
WHERE e.salary > m.salary