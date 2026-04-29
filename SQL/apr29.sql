-- Clauses -- 
show databases;
use jbk_1319;

-- between --
select * from student where age between 20 and 23;
select * from student where age not between 20 and 23;

-- in --
select * from student where age in (20,22,24);
select * from student where age not in (20,22,24);
select * from student where age in ('pune',"mumbai","delhi");
select * from student where age not in ('pune',"mumbai","delhi");
select * from student where city in ('pune',"mumbai","delhi") and age in (20,22,24);
select * from student where city in ('pune',"mumbai","delhi") or age not in (20,22,24);

-- like --
-- % - one or more character
-- _ - zero or more character
select * from student where name like '%a';
select * from student where name like 'a%';
select * from student where name like '_o%';
select * from student where name like '%o%';

-- is null --
select * from student where age is null;

-- is not null --
select * from student where age is not null;

-- distinct - gives unique value -- 
select distinct age from student;
select distinct city from student;

-- order by -- 
select * from student order by age; -- by default it gives ascending order
select * from student order by age asc;
select * from student order by age desc;
select * from student order by name;
select * from student order by name desc;
select * from student order by city;
select * from student order by city desc;

-- group by and having--
select count(city) from student group by city;
select count(city) as "Total student" , city from student group by city;
select count(city) as "Total student" , city from student group by city having count(city) >= 2;
select count(city) as "Total student" , city from student group by city;
select count(city) as "Total student" , city from student group by city having count(city) = 1;
select count(age) as "Total student" , age from student group by age;
select count(age) as "Total student" , age from student group by age having count(age) <= 2;
select count(age) as "Total student" , age from student group by age having count(age) >= 2;

-- limit -- 
select * from student limit 5;
select * from student limit 5,10; -- skip first 5 records
select * from student order by age asc limit 5;
select * from student order by id desc limit 5; -- Display last 5 records
select  max(age) from student;
select  min(age) from student;

-- nested query --
select * from student where age = (select min(age) from student);
select * from student where age = (select max(age) from student);
select  max(age) from student where age < (select  max(age) from student);
select  min(age) from student where age > (select  min(age) from student);
select * from student where age = (select  max(age) from student where age < (select  max(age) from student));
select * from student where age = (select  min(age) from student where age > (select  min(age) from student));
