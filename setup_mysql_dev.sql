-- create hbnb_dev_db db if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create hbnb_dev user in localhost with hbnb_dev_pwd password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- give hbnb_dev all privileges on  db hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- give hbnb_dev SELECT privilege on  db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
