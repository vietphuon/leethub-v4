# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees as e
LEFT JOIN Salaries as s
ON e.employee_id = s.employee_id
WHERE ISNULL(s.salary)

UNION

SELECT s.employee_id
FROM Employees as e
RIGHT JOIN Salaries as s
ON e.employee_id = s.employee_id
WHERE ISNULL(e.name)

ORDER BY employee_id ASC