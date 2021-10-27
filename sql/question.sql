CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `question`;
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
VALUES (1, 3, "A kilometer is shorter than a mile.", 2);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (2, 3, "Which of the following is a fundamental quantity", 3);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (1, 3, "A kilometer is shorter than a mile.", 2);

INSERT INTO `question` (`question_id`, `quiz_id`, `question_text`, `answer_id`) 
VALUES (2, 3, "Which of the following is a fundamental quantity", 3);
