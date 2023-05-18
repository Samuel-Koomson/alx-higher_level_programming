-- Script creates the table id_not_null on MySQL server.
-- id_not_null description: id INT with the default value 1, name VARCHAR(256)
-- mysql database name is passed as argument of mysql command
-- If table id_not_null already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
