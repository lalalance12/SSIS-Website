CREATE DATABASE IF NOT EXISTS `web_ssis_database`;

USE `web_ssis_database`;


CREATE TABLE IF NOT EXISTS college (
                code VARCHAR(15) NOT NULL PRIMARY KEY,
                name VARCHAR(50) NOT NULL
)


CREATE TABLE IF NOT EXISTS Course (
                code VARCHAR(20) NOT NULL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                college VARCHAR(50) NOT NULL,
                CONSTRAINT fk1 FOREIGN KEY (college) REFERENCES college (name) ON DELETE CASCADE ON UPDATE CASCADE
)


CREATE TABLE IF NOT EXISTS Student (
                id VARCHAR(20) NOT NULL PRIMARY KEY,
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                course VARCHAR(30) NOT NULL,
                year VARCHAR(10) NOT NULL,
                gender VARCHAR(20) NOT NULL,
                image_url VARCHAR(70) NOT NULL,
                CONSTRAINT fk2 FOREIGN KEY (course) REFERENCES course (code) ON DELETE CASCADE ON UPDATE CASCADE
)