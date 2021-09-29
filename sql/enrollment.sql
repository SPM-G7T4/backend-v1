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