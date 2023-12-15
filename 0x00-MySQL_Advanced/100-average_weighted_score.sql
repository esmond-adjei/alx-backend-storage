-- creates a sorted procedure `ComputeAverageWeightedScoreForUser`
-- that computes and store the average weighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE total_weight FLOAT;
  DECLARE total_weighted_score FLOAT;
  DECLARE average_weighted_score FLOAT;

  SELECT SUM(c.score * p.weight), SUM(p.weight)
  INTO total_weighted_score, total_weight
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = user_id;

  -- calculate average
  IF total_weight > 0 THEN
    SET average_weighted_score = total_weighted_score / total_weight;
  ELSE
    SET average_weighted_score = 0;
  END IF;

  -- apply updates
  UPDATE users
  SET average_score = average_weighted_score
  WHERE id = user_id;
END //

DELIMITER ;
