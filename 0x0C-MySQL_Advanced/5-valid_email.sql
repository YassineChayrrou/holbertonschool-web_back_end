-- SQL script
-- creates a trigger that resets attribute valid_email when the email is changed
DELIMITER $$
CREATE TRIGGER email_validation
BEFORE UPDATE
ON users FOR EACH ROW BEGIN
IF OLD.email != NEW.email THEN
    SET NEW.valid_email = 0;
END IF;
END$$
