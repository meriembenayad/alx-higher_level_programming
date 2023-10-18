-- Creates the database hbtn_0d_usa and the table cities.
-- id INT auto generated, not null, primary key.
-- state_id INT, not null, foreign key to id of states table.
-- name VARCHAR(256) not null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    state_id INT not NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
