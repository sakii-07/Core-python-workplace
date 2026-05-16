-- constraints --
use jbk_1319;

-- 3) check --
create table student(id int primary key, name text, age int check(age>=18 and age<=40),city text);

-- If table already exists --
alter table student add constraint check_student_age check (age >= 18 and age<=30);
alter table student drop check check_student_age;

-- 4) default --
create table student(id int primary key, name text, age int check(age>=18 and age<=40),city text default 'pune');
alter table student alter age set default 'pune';
alter table student alter age drop default;

-- auto_increment --
create table student(id int primary key auto_increment, name text, age int,city text);
