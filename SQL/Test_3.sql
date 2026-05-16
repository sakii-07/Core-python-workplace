use capgemini;

create table employees (id int primary key, name text, salary int, department text, location text);

INSERT INTO employees (id, name, salary, department, location) VALUES
(1, 'Amit Sharma', 50000, 'IT', 'Pune'),
(2, 'Neha Patil', 45000, 'HR', 'Mumbai'),
(3, 'Rahul Verma', 60000, 'Finance', 'Delhi'),
(4, 'Sneha Kulkarni', 55000, 'IT', 'Bangalore'),
(5, 'Vikas Singh', 48000, 'Marketing', 'Hyderabad'),
(6, 'Priya Deshmukh', 52000, 'HR', 'Pune'),
(7, 'Karan Mehta', 70000, 'Finance', 'Mumbai');

select distinct name from employees;
select count(*) as 'Total employees' from employees;
select distinct department from employees;
select department , count(*) from employees group by department;
select max(salary) as "Max salary" from employees;
select min(salary) as "Min salary" from employees;
select count(*) from employees where salary > 20000;
select avg(salary) as 'Average salary' from employees;
select * from employees order by salary desc limit 5;
select * from employees where department = "marketing";
select count(*) from employees where salary between 15000 and 50000;
select * from employees where salary is null;
select * from employees where name like 's%';
select distinct salary from employees order by salary desc;
select sum(salary)as 'Total salary' from employees;

select count(*) from employees where location = "pune";
select avg(salary) from employees where department = "marketing";
select * from employees where salary > (select avg(salary) from employees);
select * from employees where salary = (select min(salary) from employees where department = "IT");
select count(*) from employees where year = 2023;
select * from employees where year = 2023;
select sum(salary) from employees where department = "marketing" or department = "IT";
select * from employees where salary > (select avg(salary) from employees where department = "IT");
select sum(salary) as "Total salary" from employees where location = "pune";