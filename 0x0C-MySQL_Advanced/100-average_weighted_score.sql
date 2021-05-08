-- SQL script
-- creates stored procedure that computes and store average weighted score of a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
CREATE VIEW statistics
AS SELECT corrections.*, projects.weight, (corrections.score * projects.weight) AS factor
FROM corrections, projects
WHERE corrections.project_id = projects.id;
SELECT SUM(factor) / SUM(weight) INTO @average FROM statistics
WHERE statistics.user_id = user_id;
UPDATE users SET average_score = @average WHERE id = user_id;
DROP VIEW statistics;
END$$
