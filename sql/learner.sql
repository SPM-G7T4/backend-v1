CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

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