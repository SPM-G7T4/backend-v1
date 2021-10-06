CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `enrolment`;
CREATE TABLE IF NOT EXISTS `enrolment` (
    `learner_email` varchar(64) NOT NULL,
    `enrolment_date` date NOT NULL,
    `class_start_datetime` datetime NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_id` int(4) NOT NULL,
    `hr_enroler_email` varchar(64) DEFAULT NULL,
    `approver_email` varchar(64) DEFAULT NULL,
    `approved` boolean DEFAULT 0,

    PRIMARY KEY (learner_email, course_id, class_id, enrolment_date),
    FOREIGN KEY (learner_email) REFERENCES learner(email),
    FOREIGN KEY (course_id, class_id, class_start_datetime) REFERENCES class(course_id, class_id, start_datetime),
    FOREIGN KEY (hr_enroler_email) REFERENCES hr(email),
    FOREIGN KEY (approver_email) REFERENCES hr(email)
);

INSERT INTO `enrolment` (
    `learner_email`,
    `enrolment_date`, 
    `class_start_datetime`, 
    `course_id`, 
    `class_id`, 
    `hr_enroler_email`, 
    `approver_email`, 
    `approved`
) VALUES (
    "sean@smu.edu.sg", 
    CURRENT_DATE(),
    "2021-05-30 23:59:59", 
    "REP1101", 
    1,
    "avigale@smu.edu.sg",
    "joen@smu.edu.sg",
    1
);

INSERT INTO `enrolment` (
    `learner_email`,
    `enrolment_date`, 
    `class_start_datetime`, 
    `course_id`, 
    `class_id`, 
    `hr_enroler_email`, 
    `approver_email`, 
    `approved`
) VALUES (
    "niankai@smu.edu.sg", 
    CURRENT_DATE(),
    "2021-05-30 23:59:59", 
    "REP1101", 
    2,
    NULL,
    "joen@smu.edu.sg",
    1
);