# Write your MySQL query statement below
SELECT activity_date as day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY) AND activity_date <= "2019-07-27"