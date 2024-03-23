# CREATE DATABASE course_web;
USE course_web;
CREATE TABLE `users`(
    `username` varchar(32) primary key not null,
    `password` varchar(32) not null,
    `email` varchar(32) unique not null
) DEFAULT CHARSET = utf8;
CREATE TABLE `published_articles`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` varchar(32) not null,
    `content` varchar(10000) NOT NULL,
    `category` varchar(32) not null,
    `author` varchar(32) not null,
    `date` DATETIME NOT NULL
);
CREATE TABLE `deleted_articles`(
    `id` INT NOT NULL PRIMARY KEY,
    `title` varchar(32) not null,
    `content` varchar(10000) NOT NULL,
    `category` varchar(32) not null,
    `author` varchar(32) not null,
    `published_date` DATETIME NOT NULL,
    `deleted_date` DATETIME NOT NULL
);