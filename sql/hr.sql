CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `hr`;
CREATE TABLE IF NOT EXISTS `hr` (
    `email` varchar(64) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL,
    `password` varchar(32) NOT NULL
);

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("joen@smu.edu.sg", "joen", "123");

INSERT INTO `hr` (`email`, `name`, `password`) 
VALUES ("avigale@smu.edu.sg", "avigale", "123");
