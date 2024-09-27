-- This script is the setting for the MYSQL server for the project.

-- Creates database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates first primary user (must always do this)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev (school instructions specified this)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev (school instructions specify this)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges MAKES ALL CHANGES TAKE EFFECT
FLUSH PRIVILEGES;