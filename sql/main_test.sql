USE `spm_g7t4_test`;

DROP TABLE IF EXISTS `option`;
DROP TABLE IF EXISTS `question`;
DROP TABLE IF EXISTS `section`;
DROP TABLE IF EXISTS `quiz`;
DROP TABLE IF EXISTS `enrolment`;
DROP TABLE IF EXISTS `completed`;
DROP TABLE IF EXISTS `class`;
DROP TABLE IF EXISTS `prerequisite`;
DROP TABLE IF EXISTS `course`;
DROP TABLE IF EXISTS `trainer`;
DROP TABLE IF EXISTS `hr`;
DROP TABLE IF EXISTS `learner`;

-- Learner;

CREATE TABLE IF NOT EXISTS `learner` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL,
    `designation` varchar(64) NOT NULL,
    `department` varchar(64) NOT NULL
);

INSERT INTO `learner` (`email`, `name`, `password`, `designation`, `department`) 
VALUES ("niankai@smu.edu.sg", "Niankai", "123", "Junior systems engineer", "Engineering");

INSERT INTO `learner` (`email`, `name`, `password`, `designation`, `department`) 
VALUES ("sean@smu.edu.sg", "Sean", "123", "Junior electrical engineer", "Engineering");

-- HR;

CREATE TABLE IF NOT EXISTS `hr` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("joen@smu.edu.sg", "joen", "123");

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("avigale@smu.edu.sg", "avigale", "123");

-- Trainer;

CREATE TABLE IF NOT EXISTS `trainer` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `trainer` (`email`, `name`, `password`) 
VALUES ("jiale@smu.edu.sg", "Ong Jia Le", "123");

INSERT INTO `trainer` (`email`, `name`, `password`) 
VALUES ("ken@smu.edu.sg", "Ken Tich", "123");

-- Course;

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

-- Prerequisite;

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

-- Class;

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

-- Completed;

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

-- Enrolment;

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

-- Quiz;

CREATE TABLE IF NOT EXISTS `quiz` (
    `quiz_id` int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `quiz_name` varchar(64) NOT NULL
);

INSERT INTO `quiz` (`quiz_name`) 
VALUES ("Term Definitions");

INSERT INTO `quiz` (`quiz_name`) 
VALUES ("Systems");

INSERT INTO `quiz` (`quiz_name`) 
VALUES ("Units and Scales");

INSERT INTO `quiz` (`quiz_name`) 
VALUES ("Component Quiz");

INSERT INTO `quiz` (`quiz_name`) 
VALUES ("Identifying Key Users");

-- Section;

CREATE TABLE IF NOT EXISTS `section` (
    `section_id` int(4) NOT NULL,
    `section_name` varchar(64) NOT NULL,
    `quiz_id` int(4) DEFAULT NULL,
    `class_id` int(4) NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_start_datetime` datetime NOT NULL,
    
    FOREIGN KEY (class_id, course_id, class_start_datetime) REFERENCES class(class_id, course_id, start_datetime),
    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id),
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

-- Question;

CREATE TABLE IF NOT EXISTS `question` (
    `question_id` int(4) NOT NULL,
    `quiz_id` int(4) NOT NULL,
    `question_text` varchar(128) NOT NULL,
    `answer_id` int(1) NOT NULL,
    
    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id),
    PRIMARY KEY (question_id, quiz_id)
);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (1, 1, "Define 'System'", 1);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (2, 1, "Define 'Component'", 3);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (1, 2, "What is needed for a System to run?", 2);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (2, 2, "A system can only consist of inanimate objects", 2);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (1, 3, "A kilometer is shorter than a mile.", 1);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (2, 3, "Which of the following is a fundamental quantity", 3);

-- Option;

CREATE TABLE IF NOT EXISTS `option` (
    `option_id` int(4) NOT NULL,
    `question_id` int(4) NOT NULL,
    `quiz_id` int(4) NOT NULL,
    `option_value` varchar(128) NOT NULL,
    
    FOREIGN KEY (question_id, quiz_id) REFERENCES question(question_id, quiz_id),
    PRIMARY KEY (option_id, question_id, quiz_id)
);

-- Question 1 Quiz 1;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 1, "A set of things working together as parts of a mechanism or an interconnecting network");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 1, "Multiple components joined together");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 1, 1, "People and processes that serve a common purpose");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 1, 1, "Something that generates value by using electricity");

-- Question 2 Quiz 1;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 1, "Objects that are used by humans or other objects");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 1, "An inanimate object");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 2, 1, "A part or element of a larger whole");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 2, 1, "An abstraction of a real-life concept or model");

-- Question 1 Quiz 2;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 2, "Fossil Fuels");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 2, "Energy that matches the expected input of the system");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 1, 2, "Human Labour");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 1, 2, "Renewable Energy");

-- Question 2 Quiz 2;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 2, "True");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 2, "False");

-- Question 1 Quiz 3;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 3, "True");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 3, "False");

-- Question 2 Quiz 3;

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 3, "Force");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 3, "Acceleration");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 2, 3, "Luminous Intensity");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 2, 3, "Potential Difference");
