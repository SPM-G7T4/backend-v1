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
    `enrol_start_datetime` datetime NOT NULL,
    `enrol_end_datetime` datetime NOT NULL,
    
    PRIMARY KEY (class_id, course_id, start_datetime),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (trainer_email) REFERENCES trainer(email),
    CHECK (end_datetime > start_datetime),
    CHECK (enrol_end_datetime > enrol_start_datetime)
) ;

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`) 
VALUES (1, 40, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101", "2020-12-01 00:00:00", "2022-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (2, 40, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101", "2020-12-01 00:00:00", "2022-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`) 
VALUES (1, 35, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1201", "2020-12-01 00:00:00", "2022-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (1, 30, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1301", "2020-12-01 00:00:00", "2022-12-30 23:59:59");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_datetime`, `end_datetime`, `course_id`, `enrol_start_datetime`, `enrol_end_datetime`)  
VALUES (1, 30, "ken@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP2101", "2020-12-01 00:00:00", "2022-12-30 23:59:59");
