-- Creates the table unique_id:
-- id INT
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);
