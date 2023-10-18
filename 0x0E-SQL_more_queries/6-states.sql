-- Creates the database hbtn_0d_usa.
-- the table states (in the database hbtn_0d_usa)
-- id INT auto_increment primary key
-- name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
