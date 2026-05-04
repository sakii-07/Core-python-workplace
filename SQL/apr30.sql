-- constraints -- 
use jbk_1319;

drop table student;

-- primary key -- 
create table student (id int primary key, name text, age int, city text);

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

select * from student;
insert into student values(30,"sakshi jagtap",20,"solapur")

alter table student add constraint primary key (id);
alter table student drop primary key;

-- not null constraints-- 
create table student (id int primary key, name text not null, age int, city text);
select * from student;