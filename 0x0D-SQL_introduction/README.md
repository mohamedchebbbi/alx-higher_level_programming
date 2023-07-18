#0x0D. SQL - Introduction

#Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#General
 -What’s a database
 -What’s a relational database
 -What does SQL stand for
 -What’s MySQL
 -How to create a database in MySQL
 -What does DDL and DML stand for
 -How to CREATE or ALTER a table
 -How to SELECT data from a table
 -How to INSERT, UPDATE or DELETE data
 -What are subqueries
 -How to use MySQL functions

#Copyright - Plagiarism
 -You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
 -You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
 -You are not allowed to publish any content of this project.
 -Any form of plagiarism is strictly forbidden and will result in removal from the program.

#Requirements
#General
 -Allowed editors: vi, vim, emacs
 -All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
 -All your files should end with a new line
 -All your SQL queries should have a comment just before (i.e. syntax above)
 -All your files should start by a comment describing the task
 -All SQL keywords should be in uppercase (SELECT, WHERE…)
 -A README.md file, at the root of the folder of the project, is mandatory
 -The length of your files will be tested using wc

#More Info
#Comments for your SQL file:
<div>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$</div>
#Install MySQL 8.0 on Ubuntu 20.04 LTS
<div>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$</div>
#Connect to your MySQL server:
<div>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$</div>
