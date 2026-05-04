use capgemini;

create table employee (id int primary key, name varchar(16), profile varchar(16), email varchar(32) unique, salary int, age int, experiance int);

insert into employee values (1,'rani','dev','rani@gmail.com', 11000, 43,27);
insert into employee values (2,'raj','test','raj@gmail.com', 21000, 33,17),
(3,'radha','test','radha@gmail.com', 26000, 38,21),
(4,'raj','dev','raj12@gmail.com', 51000, 32,12),
(5,'john','dev','john@gmail.com', 51000, 39,27);

drop table employee;
select * from employee;

-- 1 --
alter table employee add column branch_location text;

-- 2-- 
select sum(salary) as "Total salary" from employee ;

-- 3--
select max(salary) as "Max salary" from employee where profile = "test";

-- 4--
select * from employee where experiance = (select avg(experiance) from employee);

-- 5 --
select name from employee where salary = (select max(salary) from employee);

-- 6 --
select name, experiance from employee where salary = (select min(salary) from employee);

-- 7 --
select count(*) as 'Total Empoyee' from employee;

-- 8 --
select name from employee where profile = 'test' and salary > 25000;

-- 9 --
update employee set profile = "support" where name = "radha";

-- 10 --
select salary as "Second Max salary" from employee order by salary desc limit 1,1;
select max(salary) from employee where salary < (select max(salary) from employee);

-- 11 -- 
select salary as "Second min salary" from employee order by salary limit 1,1;

-- 12 -- 
select avg(salary) from employee where profile = "dev";

-- 13 -- 
select name, salary from employee where experiance = (select min(experiance) from employee);

-- 14 --
select name from employee where age = (select min(age) from employee) and salary = (select max(salary) from employee);

-- 15 --
SET SQL_SAFE_UPDATES = 0;
delete from employee;