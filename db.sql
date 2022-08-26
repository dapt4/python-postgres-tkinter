CREATE DATABASE students_example;
CREATE TABLE students(id Serial, name text, address text, age int);

INSERT INTO students(name, address, age) VALUES ('joe', 'LA', 30);
INSERT INTO students(name, address, age) VALUES ('ryan', 'San francisco', 23);
