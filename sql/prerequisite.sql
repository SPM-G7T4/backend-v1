CREATE DATABASE IF NOT EXISTS `spm_g7t4`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_g7t4`;

DROP TABLE IF EXISTS `prerequisite`;
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