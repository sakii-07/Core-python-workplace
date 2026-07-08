create database mock_interview;
use mock_interview;

create table student (sid int primary key auto_increment, sname varchar(32), email varchar(32));
insert into student(sname,email) values("sakshi","sakshi@gmail.com"),
("divya","divya@gmail.com"),("harsh","harsh@gmail.com"),("amruta","amruta@gmail.com");

select * from student; -- context management

select substring_index(email,'@',1) as username, substring_index(email,'@',-1) as Domain from student;