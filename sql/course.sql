CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
    `course_id` char(7) NOT NULL PRIMARY KEY,
    `course_name` varchar(64) NOT NULL,
    `start_date` datetime NOT NULL,
    `end_date` datetime NOT NULL,
    `created_date` timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `course` (`course_id`, `course_name`, `start_date`, `end_date`) 
VALUES ("REP1101", "General Repairs", "2021-01-07 00:00:00", "2021-05-30 23:59:59");

INSERT INTO `course` (`course_id`, `course_name`, `start_date`, `end_date`) 
VALUES ("REP2101", "Printing Coach Repairs", "2021-01-07 00:00:00", "2021-05-30 23:59:59");