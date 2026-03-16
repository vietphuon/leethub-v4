# Write your MySQL query statement below
WITH cte AS (SELECT e.name AS Employee, d.name AS Department, e.salary AS Salary, DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS salary_rank
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM cte
WHERE salary_rank <= 3