-- SQL script
-- creates a stored procedure that calculate the average weighted score of every users
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
UPDATE users
SET average_score =
(
    SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    FROM corrections LEFT JOIN projects
    ON corrections.project_id = projects.id
    WHERE corrections.user_id = users.id
);
END$$
