-- SQL script
-- creates a function that divides and returns the first by second number
-- return 0 if second number equal 0
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
IF (b = 0)
THEN RETURN 0;
ELSE
RETURN a / b;
END IF;
END$$
