CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section` (
    `section_id` int(4) NOT NULL,
    `section_name` varchar(64) NOT NULL,
    `quiz_id` varchar(64) DEFAULT NULL,
    `class_id` int(4) NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_start_datetime` datetime NOT NULL,
    
    FOREIGN KEY (class_id, course_id, class_start_datetime) REFERENCES class(class_id, course_id, start_datetime),
    PRIMARY KEY (section_id, class_id, course_id, class_start_datetime)
) ;

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`,
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    1, "Introductions: Terms", 1, 
    1, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`, 
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    2, "Systems and Operations", 2, 
    1, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`, 
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    1, "Introductions: Terms", 1, 
    2, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`, 
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    1, "Introductions: Measurments", 3, 
    1, "REP1201", "2021-01-07 00:00:00");

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`, 
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    1, "Introductions: Components", 4, 
    1, "REP1301", "2021-01-07 00:00:00");

INSERT INTO `section` (
    `section_id`, `section_name`, `quiz_id`, 
    `class_id`, `course_id`, `class_start_datetime`) 
VALUES (
    1, "Introductions: Users", 5, 
    1, "REP2101", "2021-01-07 00:00:00");