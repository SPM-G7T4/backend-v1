CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `quiz`;
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