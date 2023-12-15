-- creates a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE user_id_var INT;
  DECLARE done INT DEFAULT FALSE;
  DECLARE cur CURSOR FOR SELECT id FROM users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO user_id_var;

    IF done THEN
      LEAVE read_loop;
    END IF;

    CALL ComputeAverageWeightedScoreForUser(user_id_var);
  END LOOP;

  CLOSE cur;
END //

DELIMITER ;

