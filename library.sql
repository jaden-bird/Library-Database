DROP DATABASE IF EXISTS library;
CREATE DATABASE library;
USE library;

CREATE TABLE Users (username VARCHAR(20) PRIMARY KEY NOT NULL, upassword VARCHAR(20) NOT NULL, ufname VARCHAR(25) NOT NULL, ulname VARCHAR(25), rflag BOOLEAN, lflag BOOLEAN);
CREATE TABLE Author (aid int PRIMARY KEY NOT NULL, afname VARCHAR(25) NOT NULL, alname VARCHAR(25) NOT NULL);
CREATE TABLE Publisher (pid int PRIMARY KEY NOT NULL, pname VARCHAR(50));
CREATE TABLE Book (title VARCHAR(50) PRIMARY KEY NOT NULL, aid int NOT NULL, date_published DATE NOT NULL, checked_out_by VARCHAR(20), check_out_date DATE,
FOREIGN KEY (aid) REFERENCES Author(aid));
CREATE TABLE Published_By (pid int NOT NULL, title VARCHAR(50) NOT NULL,
PRIMARY KEY (pid, title),
FOREIGN KEY (pid) REFERENCES Publisher(pid), FOREIGN KEY(title) REFERENCES Book(title));
CREATE TABLE Genre (title VARCHAR(50) PRIMARY KEY NOT NULL, genre VARCHAR(25) NOT NULL,
FOREIGN KEY (title) REFERENCES Book(title));
CREATE TABLE Manages (lusername VARCHAR(20) NOT NULL, title VARCHAR(50) NOT NULL,
PRIMARY KEY (lusername, title),
FOREIGN KEY (lusername) REFERENCES Users(username), FOREIGN KEY(title) REFERENCES Book(title));
CREATE TABLE Returns_Table (uusername VARCHAR(20) NOT NULL, title VARCHAR(50) NOT NULL, return_date DATE NOT NULL,
PRIMARY KEY (uusername, title),
FOREIGN KEY (uusername) REFERENCES Users(username), FOREIGN KEY(title) REFERENCES Book(title));

INSERT INTO Users VALUES ('reader1', 'rpassword', 'Frank', 'Smith', TRUE, FALSE);
INSERT INTO Users VALUES ('reader2', '123456789', 'Emily', 'Johnson', TRUE, FALSE);
INSERT INTO Users VALUES ('TheLibrarian', 'pass', 'Charlotte', 'Williams', FALSE, TRUE);

INSERT INTO Author VALUES (1, 'William', 'Shakespeare');
INSERT INTO Author VALUES (2, 'Mark', 'Twain');
INSERT INTO Author VALUES (3, 'Jane', 'Austen');

INSERT INTO Publisher VALUES (1, 'Publishing Company #1');
INSERT INTO Publisher VALUES (2, 'Publisher CO');

INSERT INTO Book VALUES ('Macbeth', 1, '1623-10-15', 'reader1', '2025-11-20');
INSERT INTO Book(title, aid, date_published) VALUES ('Life on the Mississippi', 2, '1883-04-12');
INSERT INTO Book VALUES ('Emma', 3, '1815-12-24', 'reader2', '2025-12-03');

INSERT INTO Published_By VALUES (1, 'Macbeth');
INSERT INTO Published_By VALUES (2, 'Life on the Mississippi');
INSERT INTO Published_By VALUES (2, 'Emma');

INSERT INTO Genre VALUES ('Macbeth', 'Tragedy');
INSERT INTO Genre VALUES ('Life on the Mississippi', 'Biography');
INSERT INTO Genre Values ('Emma', 'Romance');

INSERT INTO Manages VALUES ('TheLibrarian', 'Macbeth');
INSERT INTO Manages VALUES ('TheLibrarian', 'Life on the Mississippi');
INSERT INTO Manages VALUES ('TheLibrarian', 'Emma');

INSERT INTO Returns_Table VALUES ('reader1', 'Macbeth', '2025-12-20');
INSERT INTO Returns_Table VALUES ('reader2', 'Emma', '2026-01-03');

ALTER TABLE Book ADD COLUMN return_date DATE;