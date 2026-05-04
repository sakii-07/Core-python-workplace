-- Test :- 1 --
create database capgemini;
use capgemini;

create table employee (id int primary key, name varchar(16), profile varchar(16), email varchar(32) unique, salary int, age int, experiance int);

insert into employee values (1,'rani','dev','rani@gmail.com', 11000, 43,27);
insert into employee values (2,'raj','test','raj@gmail.com', 21000, 33,17),
(3,'radha','test','radha@gmail.com', 26000, 38,21),
(4,'raj','dev','raj12@gmail.com', 51000, 32,12),
(5,'john','dev','john@gmail.com', 51000, 39,27);

select * from employee;

SET SQL_SAFE_UPDATES = 0;

select name from employee where salary > 20000;
select * from employee where salary = 51000;
select name, experiance from employee where age > 35; 
select * from employee where profile = 'dev';
select * from employee where profile = 'test';
select * from employee where salary >= 25000;
select name , email from employee where salary <> 51000;
update employee set salary = salary + 10000 where experiance < 20;
delete from employee where experiance = 21;
update employee set salary = salary - 21000 where name = 'john'; 
