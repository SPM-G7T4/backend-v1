DROP DATABASE IF EXISTS `spm_g7t4`;
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
VALUES ("jiale@smu.edu.sg", "Ong Jia Le", "123");

INSERT INTO `trainer` (`email`, `name`, `password`) 
VALUES ("ken@smu.edu.sg", "Ken Tich", "123");

-- Course
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

-- Prerequisite
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `prerequisite`;
CREATE TABLE IF NOT EXISTS `prerequisite` (
    `prerequisite_id` char(7) NOT NULL,
    `postrequisite_id` char(7) NOT NULL,
    `created_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (prerequisite_id, postrequisite_id),
    FOREIGN KEY (prerequisite_id) REFERENCES course(course_id),
    FOREIGN KEY (postrequisite_id) REFERENCES course(course_id),
    CHECK (prerequisite_id <> postrequisite_id)
);

INSERT INTO `prerequisite` (`prerequisite_id`, `postrequisite_id`) 
VALUES ("REP1101", "REP1301");

INSERT INTO `prerequisite` (`prerequisite_id`, `postrequisite_id`) 
VALUES ("REP1201", "REP1301");

-- Class
DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
    `class_id` int(4) NOT NULL,
    `class_size` int(3) NOT NULL,
    `trainer_email` varchar(64) DEFAULT NULL,
    `start_datetime` datetime NOT NULL,
    `end_datetime` datetime NOT NULL,
    `course_id` char(7)NOT NULL,
    `enrol_start_datetime` datetime NOT NULL,
    `enrol_end_datetime` datetime NOT NULL,
    
    PRIMARY KEY (class_id, course_id, start_datetime),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (trainer_email) REFERENCES trainer(email),
    CHECK (end_datetime > start_datetime),
    CHECK (enrol_end_datetime > enrol_start_datetime)
) ;

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`) 
VALUES (1, 40, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101", "2020-12-01 00:00:00", "2020-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (2, 40, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101", "2020-12-01 00:00:00", "2020-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`) 
VALUES (1, 35, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1201", "2020-12-01 00:00:00", "2020-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (1, 30, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1301", "2020-12-01 00:00:00", "2020-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (1, 30, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP2101", "2020-12-01 00:00:00", "2020-12-30 23:59:59");

-- Completed
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `completed`;
CREATE TABLE IF NOT EXISTS `completed` (
    `learner_email` varchar(64) NOT NULL,
    `course_id` char(7) NOT NULL,
    `completion_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
    

    PRIMARY KEY (learner_email, course_id),
    FOREIGN KEY (learner_email) REFERENCES learner(email),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO `completed` (
    `learner_email`,
    `course_id` 
) VALUES (
    "sean@smu.edu.sg", 
    "REP1101"
);

-- Enrolment
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `enrolment`;
CREATE TABLE IF NOT EXISTS `enrolment` (
    `learner_email` varchar(64) NOT NULL,
    `enrolment_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
    `class_start_datetime` datetime NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_id` int(4) NOT NULL,
    `hr_enroler_email` varchar(64) DEFAULT NULL,
    `approver_email` varchar(64) DEFAULT NULL,
    `status` varchar(10) DEFAULT NULL,

    PRIMARY KEY (learner_email, course_id, class_id, class_start_datetime),
    FOREIGN KEY (learner_email) REFERENCES learner(email),
    FOREIGN KEY (course_id, class_id, class_start_datetime) REFERENCES class(course_id, class_id, start_datetime),
    FOREIGN KEY (hr_enroler_email) REFERENCES hr(email),
    FOREIGN KEY (approver_email) REFERENCES hr(email)
);

INSERT INTO `enrolment` (
    `learner_email`,
    `enrolment_datetime`, 
    `class_start_datetime`, 
    `course_id`, 
    `class_id`, 
    `hr_enroler_email`, 
    `approver_email`, 
    `status`
) VALUES (
    "sean@smu.edu.sg", 
    CURRENT_TIMESTAMP,
    "2021-01-07 00:00:00", 
    "REP1101", 
    1,
    NULL,
    "joen@smu.edu.sg",
    "enrolled"
);

INSERT INTO `enrolment` (
    `learner_email`,
    `enrolment_datetime`, 
    `class_start_datetime`, 
    `course_id`, 
    `class_id`, 
    `hr_enroler_email`, 
    `approver_email`, 
    `status`
) VALUES (
    "niankai@smu.edu.sg", 
    CURRENT_TIMESTAMP,
    "2021-01-07 00:00:00", 
    "REP1101", 
    2,
    NULL,
    "joen@smu.edu.sg",
    "enrolled"
);

-- Section
CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section` (
    `section_id` int(4) NOT NULL,
    `section_name` varchar(64) NOT NULL,
    `quiz_name` varchar(64) DEFAULT NULL,
    `class_id` int(4) NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_start_datetime` datetime NOT NULL,
    
    FOREIGN KEY (class_id, course_id, class_start_datetime) REFERENCES class(class_id, course_id, start_datetime),
    PRIMARY KEY (section_id, class_id, course_id, class_start_datetime)
) ;

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (1, "Introductions: Terms", "Term Definitions", 1, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (2, "Systems and Operations", "Systems", 1, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (1, "Introductions: Terms", "Term Definitions", 2, "REP1101", "2021-01-07 00:00:00");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (1, "Introductions: Measurments", "Units and Scales", 1, "REP1201", "2021-01-07 00:00:00");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (1, "Introductions: Components", "Component Quiz", 1, "REP1301", "2021-01-07 00:00:00");

INSERT INTO `section` (`section_id`, `section_name`, `quiz_name`, `class_id`, `course_id`, `class_start_datetime`) 
VALUES (1, "Introductions: Users", "Identifying Key Users", 1, "REP2101", "2021-01-07 00:00:00");