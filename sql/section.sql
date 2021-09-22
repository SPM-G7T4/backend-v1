CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section` (
    `section_id` int(4) NOT NULL,
    `section_name` varchar(64) NOT NULL,
    `quiz_name` varchar(64) DEFAULT NULL,
    `class_id` int(4) NOT NULL,
    `course_id` char(7) NOT NULL,
    
    FOREIGN KEY (class_id, course_id) REFERENCES class(class_id, course_id),
    PRIMARY KEY (section_id, class_id, course_id)
) ;

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (1, "Introductions: Terms", "Term Definitions", 1, "REP1101");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (2, "Systems and Operations", "Systems", 1, "REP1101");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (1, "Introductions: Users", "Identifying Key Users", 1, "REP2101");
