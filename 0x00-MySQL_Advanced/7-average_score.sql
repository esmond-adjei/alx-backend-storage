-- creates a stored procedure `ComputeAverageScoreForUser`
-- that computes and store the average score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE total_score INT;
  DECLARE count_corrections INT;
  DECLARE average_score FLOAT;

  -- calc: total score and correction counts
  SELECT SUM(score), COUNT(*) INTO total_score, count_corrections
  FROM corrections
  WHERE user_id = user_id;

  -- calc: average
  IF count_corrections > 0 THEN
    SET average_score = total_score / count_corrections;
  ELSE
    SET average_score = 0;
  END IF;

  -- apply changes
  UPDATE users
  SET average_score = average_score
  WHERE id = user_id;
END //

DELIMITER ;
