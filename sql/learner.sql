CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `learner`;
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