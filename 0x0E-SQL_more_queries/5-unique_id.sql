-- Script creates the table unique_id on MySQL server.
-- unique_id description: 
-- id INT with the default value 1 and must be unique
--  name VARCHAR(256)
-- mysql is passed as database name as argument of mysql command
-- If the table unique_id already exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));