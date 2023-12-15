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

  -- calc: average score and store in `average_score`
  SELECT AVG(score) INTO average_score
  FROM corrections
  WHERE corrections.user_id = user_id;

  -- apply changes
  UPDATE users
  SET average_score = average_score
  WHERE id = user_id;
END //

DELIMITER ;
