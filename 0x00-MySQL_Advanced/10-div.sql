-- creates a functio SafeDiv that divides (and returns)
-- the first by the second number or returns 0
-- if the second number is equal to 0.
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,4) DETERMINISTIC
BEGIN
  DECLARE result DECIMAL(10, 4);
  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = (a * 1.0 / b);
  END IF;

  RETURN result;
END //

DELIMITER ;
