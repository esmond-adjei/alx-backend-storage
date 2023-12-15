-- creates a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE total_weighted_score FLOAT(10, 6);
  DECLARE total_weight FLOAT(10, 6);
  DECLARE total_weighted_score_sum FLOAT(10, 6);
  DECLARE total_weight_sum FLOAT(10, 6);
  DECLARE user_id INT;
  DECLARE project_id INT;
  DECLARE project_weight INT;
  DECLARE project_score FLOAT(10, 6);
  DECLARE cur CURSOR FOR SELECT user_id, project_id, weight, score FROM corrections JOIN projects ON corrections.project_id = projects.id;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET @done = TRUE;

  SET total_weighted_score_sum = 0;
  SET total_weight_sum = 0;

  OPEN cur;
  FETCH cur INTO user_id, project_id, project_weight, project_score;
  WHILE NOT @done DO
    SET total_weighted_score = total_weighted_score + (project_weight * project_score);
    SET total_weight = total_weight + project_weight;
    FETCH cur INTO user_id, project_id, project_weight, project_score;
  END WHILE;
  CLOSE cur;

  SELECT AVG(total_weighted_score / total_weight) INTO total_weighted_score_sum FROM users;
  UPDATE users SET average_score = total_weighted_score_sum;
END //

DELIMITER ;
