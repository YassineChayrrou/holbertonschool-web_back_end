-- SQL script that create a stored procedure
-- AddBonus stored procedure that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, project_name VARCHAR(100), score INT)
BEGIN
IF NOT EXISTS(SELECT id FROM projects WHERE name = project_name) THEN
INSERT INTO projects (name) VALUES (project_name);
END IF;
SELECT id INTO @id FROM projects WHERE name = project_name;
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @id, score);
END$$
