-- updates valid_email field whenever email is changed
-- for a user.
DELIMETER //

CREATE TRIGGER update_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
  BEGIN
    IF NEW.email <> OLD.email THEN
      SET NEW.valid_email = 0;
    END IF;
  END;
//

DELIMETER ;
