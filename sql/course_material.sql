DROP TABLE IF EXISTS `course_material`;
CREATE TABLE IF NOT EXISTS `course_material` (
    `material_id` int(4) NOT NULL,
    `section_id` int(4) NOT NULL,
    `class_id` int(4) NOT NULL,
    `course_id` char(7) NOT NULL,
    `class_start_datetime` datetime NOT NULL,
    `title` varchar(64) NOT NULL,
    `view_link` varchar(256) NOT NULL,
    `download_link` varchar(256) NOT NULL,

    FOREIGN KEY (section_id, class_id, course_id, class_start_datetime) REFERENCES section(section_id, class_id, course_id, class_start_datetime),
    PRIMARY KEY (material_id, section_id, class_id, course_id, class_start_datetime)
);

INSERT INTO `course_material` (`material_id`, `section_id`, `class_id`, `course_id`, `class_start_datetime`, `title`, `view_link`, `download_link`) 
VALUES (
    1,
    1,
    1, 
    "REP1101",
    "2021-01-07 00:00:00",
    "01 Types of Printer - Slides",
    "https://docs.google.com/presentation/d/e/2PACX-1vRvCHL22QsF1IQF_AKNiMjI29OxBXNdUxD_QKryPMkYn70aLJNLAwsr_rK-sjmwjQ/pub?start=false&loop=false&delayms=3000",
    "https://spm-g7t4.s3.amazonaws.com/All+in+One+-+Types+of+Printer.pptx"
    );

INSERT INTO `course_material` (`material_id`, `section_id`, `class_id`, `course_id`, `class_start_datetime`, `title`, `view_link`, `download_link`) 
VALUES (
    2,
    1,
    1, 
    "REP1101",
    "2021-01-07 00:00:00",
    "02 Uses of Printer - Slides",
    "https://docs.google.com/presentation/d/e/2PACX-1vRrj8RM3g7Y1IxCk4dNfjiegv5z4M0FbRqdFLeREQHjjVP24Hx-zvq0GFyTv9esKQ/pub?start=false&loop=false&delayms=3000",
    "https://spm-g7t4.s3.amazonaws.com/All+in+One+-+Uses+of+Printers.pptx"
    );