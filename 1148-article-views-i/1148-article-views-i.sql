# Write your MySQL query statement below
SELECT author_id as id
FROM Views
GROUP BY author_id, viewer_id
HAVING author_id = viewer_id
ORDER BY author_id ASC