CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `option`;
CREATE TABLE IF NOT EXISTS `option` (
    `option_id` int(4) NOT NULL,
    `question_id` int(4) NOT NULL,
    `quiz_id` int(4) NOT NULL,
    `option_value` varchar(128) NOT NULL,
    
    FOREIGN KEY (question_id, quiz_id) REFERENCES question(question_id, quiz_id),
    PRIMARY KEY (option_id, question_id, quiz_id)
);

-- Question 1 Quiz 1
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 1, "A set of things working together as parts of a mechanism or an interconnecting network");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 1, "Multiple components joined together");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 1, 1, "People and processes that serve a common purpose");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 1, 1, "Something that generates value by using electricity");

-- Question 2 Quiz 1
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 1, "Objects that are used by humans or other objects");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 1, "An inanimate object");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 2, 1, "A part or element of a larger whole");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 2, 1, "An abstraction of a real-life concept or model");

-- Question 1 Quiz 2
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 2, "Fossil Fuels");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 2, "Energy that matches the expected input of the system");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 1, 2, "Human Labour");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 1, 2, "Renewable Energy");

-- Question 2 Quiz 2
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 2, "True");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 2, "False");

-- Question 1 Quiz 3
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 1, 3, "True");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 1, 3, "False");

-- Question 2 Quiz 3
INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (1, 2, 3, "Force");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (2, 2, 3, "Acceleration");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (3, 2, 3, "Luminous Intensity");

INSERT INTO `option` (`option_id`, `question_id`, `quiz_id`, `option_value`) 
VALUES (4, 2, 3, "Potential Difference");
