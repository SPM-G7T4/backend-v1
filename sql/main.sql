CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

-- Learner
DROP TABLE IF EXISTS `learner`;
CREATE TABLE IF NOT EXISTS `learner` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `learner` (`email`, `name`, `password`) 
VALUES ("niankai@smu.edu.sg", "niankai", "123");

INSERT INTO `learner` (`email`, `name`, `password`) 
VALUES ("sean@smu.edu.sg", "sean", "123");

-- HR
DROP TABLE IF EXISTS `hr`;
CREATE TABLE IF NOT EXISTS `hr` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("joen@smu.edu.sg", "joen", "123");

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("avigale@smu.edu.sg", "avigale", "123");

-- Trainer
DROP TABLE IF EXISTS `trainer`;
CREATE TABLE IF NOT EXISTS `trainer` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `trainer` (`email`, `name`, `password`) 
VALUES ("jiale@smu.edu.sg", "jiale", "123");

INSERT INTO `trainer` (`email`, `name`, `password`) 
VALUES ("swarna@smu.edu.sg", "swarna", "123");

-- Course
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

-- Class
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
    `class_id` int(4) NOT NULL,
    `class_size` int(3) NOT NULL,
    `trainer_email` varchar(64) DEFAULT NULL,
    `start_datetime` datetime NOT NULL,
    `end_datetime` datetime NOT NULL,
    `course_id` char(7)NOT NULL,
    
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (trainer_email) REFERENCES trainer(email),
    CHECK (end_date > start_date),
    PRIMARY KEY (class_id, course_id)
) ;

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`) 
VALUES (1, 40, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`)  
VALUES (2, 40, "swarna@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`)  
VALUES (1, 30, "swarna@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP2101");


-- Enrollment
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE IF NOT EXISTS `enrollment` (
    `learner_email` varchar(64) NOT NULL,
    `enrollment_date` date NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_id` int(4) NOT NULL,
    `hr_enroller_email` varchar(64) DEFAULT NULL,

    PRIMARY KEY (learner_email, course_id, class_id, enrollment_date),
    FOREIGN KEY (learner_email) REFERENCES learner(email),
    FOREIGN KEY (course_id, class_id) REFERENCES class(course_id, class_id),
    FOREIGN KEY (hr_enroller_email) REFERENCES hr(email)
);

INSERT INTO `enrollment` (`learner_email`, `enrollment_date`, `course_id`, `class_id`) 
VALUES ("sean@smu.edu.sg", CURRENT_DATE(), "REP1101", 1);

INSERT INTO `enrollment` (`learner_email`, `enrollment_date`, `course_id`, `class_id`) 
VALUES ("niankai@smu.edu.sg", CURRENT_DATE(), "REP1101", 2);

-- Section
DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section` (
    `section_id` int(4) NOT NULL,
    `section_name` varchar(64) NOT NULL,
    `quiz_name` varchar(64) DEFAULT NULL,
    `class_id` int(4)NOT NULL,
    `course_id` char(7)NOT NULL,
    
    FOREIGN KEY (class_id, course_id) REFERENCES class(class_id, course_id),
    PRIMARY KEY (section_id, class_id, course_id)
) ;

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (1, "Introductions: Terms", "Term Definitions", 1, "REP1101");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (2, "Systems and Operations", "Systems", 1, "REP1101");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`) 
VALUES (1, "Introductions: Users", "Identifying Key Users", 1, "REP2101");

