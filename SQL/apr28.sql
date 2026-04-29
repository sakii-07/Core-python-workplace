create database jbk_1319;
show databases;
desc jbk_1319;
use jbk_1319;

create table student (id int, name text, age int, city text);
show tables;
desc student;

-- insert command --
INSERT INTO student (id, name, age, city) VALUES
(1, 'Amit Sharma', 20, 'Pune'),
(2, 'Neha Patil', 21, 'Mumbai'),
(3, 'Rahul Verma', 22, 'Delhi'),
(4, 'Sneha Kulkarni', 19, 'Nagpur'),
(5, 'Rohit Singh', 23, 'Bangalore'),
(6, 'Priya Mehta', 20, 'Ahmedabad'),
(7, 'Karan Joshi', 24, 'Hyderabad'),
(8, 'Pooja Deshmukh', 21, 'Nashik'),
(9, 'Vikas Yadav', 22, 'Lucknow'),
(10, 'Anjali Gupta', 19, 'Jaipur'),
(11, 'Suresh Reddy', 23, 'Chennai'),
(12, 'Meena Iyer', 20, 'Coimbatore'),
(13, 'Arjun Nair', 21, 'Kochi'),
(14, 'Kavita Mishra', 22, 'Varanasi'),
(15, 'Deepak Chavan', 24, 'Kolhapur'),
(16, 'Shweta More', 19, 'Satara'),
(17, 'Nikhil Jadhav', 23, 'Solapur'),
(18, 'Ritu Saxena', 20, 'Kanpur'),
(19, 'Manoj Tiwari', 21, 'Bhopal'),
(20, 'Asha Pillai', 22, 'Trivandrum'),
(21, 'Yogesh Pawar', 24, 'Aurangabad'),
(22, 'Divya Shetty', 19, 'Mangalore'),
(23, 'Harish Kumar', 23, 'Patna'),
(24, 'Simran Kaur', 21, 'Chandigarh'),
(25, 'Gaurav Jain', 22, 'Indore'),
(26, 'Tanvi Shah', 20, 'Surat'),
(27, 'Akash Thakur', 24, 'Ranchi'),
(28, 'Rekha Bansal', 19, 'Amritsar'),
(29, 'Sanjay Dubey', 23, 'Gwalior'),
(30, 'Payal Agarwal', 21, 'Udaipur');

-- alter command -- 
alter table student add marks int;
alter table student rename std;
alter table student rename column marks to mark;
alter table student drop mark;
alter table student modify name varchar(16);

-- drop command - used to delete complete table or databases -- 
drop table student;
drop database db_name;

-- truncate command - used to delete data from student structue remains constant --
truncate table std;

-- update commnad --
update student set city = "pune";
update student set city ="mumbai" where id = 15;
update student set city="Delhi" where id=10 and name="Ananya Iyer";
update student set city="Jodhpur" where id=17 or age=22;

-- delete command --
delete from student;
delete from student where age = 20 and city = bid;
delete from student where age = 20 or city = bid;

-- aggrigate functions -- 
INSERT INTO student (id, name, age, city) VALUES (31, 'Sakshi Jagtap', null, 'Mumbai');
-- aggridate function does not count null --
select min(age) as "min age" from student;
select max(age) as "max age" from student;
select count(id) as "total students" from student;
select avg(age) as "avg of age" from student;
select sum(age) as "sum of age" from student;

select * from student;
select name , age from student;
select name , id, age from student;

-- where cluase --
select * from student where age > 22;
select * from student where age >= 22;
select * from student where age < 22;
select * from student where age <= 22;
select * from student where age != 22;
select * from student where age >= 22 and city="mumbai";
select * from student where age >= 22 or city="dilhi";
select * from student where age <= 22 and city="pune";
select * from student where age < 22 or city="jodhpur";

select * from student where age > 20 and age < 23;
select * from student where age < 20 or age > 23;
select * from student where age = 22 or age = 21 or age = 20;
select * from student where age <> 22 or age <> 21 or age <> 20;
select * from student where age not in (22,21,20);