use jbk_1319;

-- 5) unique constarint --
create table student (id int primary key, name text, email text unique, age int);
alter table student add constraint stud_email unique (email);
alter table student drop index stud_email;

-- join --
create table customers(id int primary key, name text, city text);
INSERT INTO customers (id, name, city) VALUES
(1, 'Amit Sharma', 'Pune'),
(2, 'Neha Patil', 'Mumbai'),
(3, 'Rahul Verma', 'Delhi'),
(4, 'Sneha Joshi', 'Nagpur'),
(5, 'Vikas Singh', 'Bangalore'),
(6, 'Sakshi Jagtap', 'Pune'),
(7, 'Durva Jagtap', 'Delhi');

drop table customers;

drop table orders;
create table orders (id int, prise double, cust_id int);
INSERT INTO orders (id, prise, cust_id) VALUES
(101, 2500.50, 1),
(102, 1200.00, 2),
(103, 560.75, 3),
(104, 999.99, 1),
(105, 3000.00, 5),
(106, 1500.25, 4),
(107, 700.00, 2);

select * from customers;
select * from orders;

-- join --
-- 1) Inner join
select customers.id, customers.name, orders.prise from customers inner join orders on customers.id = orders.cust_id;

-- 2) Left join
select customers.id, customers.name, orders.prise from customers left join orders on customers.id = orders.cust_id;

-- 3) Right join
select customers.id, customers.name, orders.prise from customers right join orders on customers.id = orders.cust_id;

-- 4) cross join
select customers.id, customers.name, orders.prise from customers cross join orders;

-- 5) full join
select customers.id, customers.name, orders.prise from customers left join orders on customers.id = orders.cust_id
union 
select customers.id, customers.name, orders.prise from customers right join orders on customers.id = orders.cust_id;
 
 -- any
select name, age, salary from employee where salary < any (select salary from employee where d_id = 105);
select name, age, salary from employee where salary > any (select salary from employee where d_id = 105);
select name, age, salary from employee where salary = any (select salary from employee where d_id = 105);

 -- all
select name, age, salary from employee where salary < all (select salary from employee where d_id = 105);
select name, age, salary from employee where salary > all (select salary from employee where d_id = 105);
select name, age, salary from employee where salary = all (select salary from employee where d_id = 105);

-- pip mysql connector