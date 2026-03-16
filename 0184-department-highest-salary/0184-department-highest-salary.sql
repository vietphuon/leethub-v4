# Write your MySQL query statement below
WITH cte AS (
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id
# GROUP BY d.name
)
SELECT Department, Employee, MAX(Salary)
FROM cte
GROUP BY Department, Employee