-- creates a table users with the following requirements:
-- * id: integer, never null, auto increment and is primary key
-- * email: string 255 chars, never null and unique
-- * name: string 255 chars
-- * country: enums -> US, CO, TN, never null, default=first in enums
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
