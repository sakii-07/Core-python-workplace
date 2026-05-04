-- foreing key --
create table department (id int primary key, name text);

insert into department values(1,"dev"),
(2,"test"), (3,"manager"),(4,"support");

select * from department;

create table emp (id int primary key, name text, salary double, d_id int, foreign key(d_id) references department(id));

show tables;

INSERT INTO emp (id, name, salary, d_id) VALUES
(1, 'Amit', 45000, 1),
(2, 'Neha', 52000, 2),
(3, 'Rahul', 60000, 3),
(4, 'Priya', 48000, 4),
(5, 'Suresh', 75000, 2),
(6, 'Anjali', 67000, 3),
(7, 'Vikas', 55000, 1),
(8, 'Sneha', 72000, 2),
(9, 'Karan', 80000, 3),
(10, 'Pooja', 47000, 1),
(11, 'Rohit', 53000, 2),
(12, 'Meena', 62000, 4),
(13, 'Arjun', 71000, 1),
(14, 'Kavita', 68000, 2),
(15, 'Deepak', 59000, 3),
(16, 'Nikita', 64000, 1),
(17, 'Manoj', 58000, 4),
(18, 'Swati', 77000, 3),
(19, 'Ajay', 49000, 4),
(20, 'Divya', 66000, 2);

select * from emp;

-- If table already exists --
alter table emp add d_id int;
alter table emp add constraint fk_depid foreign key(d_id) references deparment(id);
alter table emp drop foreign key fk_depid;

-- We can delete or update records in the parent table only when there are no matching records in the child table -- 
-- for update - on update cascade --
create table emp (id int primary key, name text, salary double, d_id int, foreign key(d_id) references department(id) on update cascade);
update deparment set id = 203 where name = "dev";

-- for delete - on delete cascade --
create table emp (id int primary key, name text, salary double, d_id int, foreign key(d_id) references department(id) on delete cascade);
delete from department where id = 103;

select e.name, e.salary, d.name from emp as e join department as d on d.id = e.d_id;