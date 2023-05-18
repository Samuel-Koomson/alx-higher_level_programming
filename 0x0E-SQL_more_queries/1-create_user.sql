-- Script which creates MySQL server user, user_0d_1.
-- user_0d_1 has all privileges on MySQL server
-- User_0d_1 password is set to user_0d_1_pwd
-- If user_0d_1 already exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
