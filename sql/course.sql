CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
    `course_id` char(7) NOT NULL PRIMARY KEY,
    `course_name` varchar(64) NOT NULL,
    `created_datetime` timestamp DEFAULT CURRENT_TIMESTAMP,
    `description` varchar(512) NOT NULL
);

INSERT INTO `course` (`course_id`, `course_name`, `description`) 
VALUES ("REP1101", "Printer Concepts and Terminology","Briefly describes the relationship between printers, and their assigned lines, processes and statuses.");

INSERT INTO `course` (`course_id`, `course_name`, `description`) 
VALUES ("REP1201", "Printer Operations", "Generic Description for REP1201");

INSERT INTO `course` (`course_id`, `course_name`, `description`) 
VALUES ("REP1301", "Printer Startup Tutorial", "Generic Description for REP1301");

INSERT INTO `course` (`course_id`, `course_name`, `description`) 
VALUES ("REP2101", "Printing Coach Repairs", "Generic Description for REP2101");
