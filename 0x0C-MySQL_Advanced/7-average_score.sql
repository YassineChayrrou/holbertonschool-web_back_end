-- SQL script
-- Creates stored procedure that computes average score of a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT AVG(score) FROM corrections c WHERE c.user_id = user_id)
WHERE id = user_id;
END$$
DELIMITER ;
