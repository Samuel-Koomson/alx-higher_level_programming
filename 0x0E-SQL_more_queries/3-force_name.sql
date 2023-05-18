-- Script creates the table force_name on MySQL server.
-- force_name description: id INT, name VARCHAR(256) Not Null
-- mysql database is passed as argument of mysql command
-- If table force_name already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
