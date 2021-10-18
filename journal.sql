CREATE TABLE `Journal` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL
);

INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Excited");
INSERT INTO `Mood` VALUES (null, "Calm");
INSERT INTO `Mood` VALUES (null, "Grateful");
INSERT INTO `Mood` VALUES (null, "Angry");
INSERT INTO `Mood` VALUES (null, "Frustrated");
INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Embarassed");
INSERT INTO `Mood` VALUES (null, "Ashamed");
INSERT INTO `Mood` VALUES (null, "Guilty");
INSERT INTO `Mood` VALUES (null, "Sleepy");
INSERT INTO `Mood` VALUES (null, "Content");
INSERT INTO `Mood` VALUES (null, "Neutral");
INSERT INTO `Mood` VALUES (null, "Restless");



INSERT INTO `Journal` VALUES (null, "01/01/2021", "Happy New Year", 1);
INSERT INTO `Journal` VALUES (null, "08/21/2021", "Happy birthday, Erin", 13);
INSERT INTO `Journal` VALUES (null, "07/29/2021", "It's a beautiful summer day", 5);
INSERT INTO `Journal` VALUES (null, "03/24/2021", "I like trees", 10);
INSERT INTO `Journal` VALUES (null, "07/20/2021", "Po-TA-TOES", 12);




