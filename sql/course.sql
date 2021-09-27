CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
    `course_id` char(7) NOT NULL PRIMARY KEY,
    `course_name` varchar(64) NOT NULL,
    `created_date` timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `course` (`course_id`, `course_name`) 
VALUES ("REP1101", "General Repairs");

INSERT INTO `course` (`course_id`, `course_name`) 
VALUES ("REP2101", "Printing Coach Repairs");