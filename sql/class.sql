CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
    `class_id` int(4) NOT NULL,
    `class_size` int(3) NOT NULL,
    `trainer_email` varchar(50) DEFAULT NULL,
    `start_date` date NOT NULL,
    `end_date` date NOT NULL,
    `course_id` char(7)NOT NULL,
    
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (trainer_email) REFERENCES trainer(email),
    CHECK (end_date > start_date),
    PRIMARY KEY (class_id, course_id)
) ;

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_date`, `end_date`, `course_id`) 
VALUES (1, 40, "jiale@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_date`, `end_date`, `course_id`)  
VALUES (2, 40, "swarna@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP1101");

INSERT INTO `class` (`class_id`, `class_size`, `trainer_email`, `start_date`, `end_date`, `course_id`)  
VALUES (1, 30, "swarna@smu.edu.sg", "2021-01-07 00:00:00", "2021-05-30 23:59:59", "REP2101");
