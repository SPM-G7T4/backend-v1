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