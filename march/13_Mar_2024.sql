create database common;

use common;

create table Product(product_key int,primary key(product_key));
create table Customer(customer_id int,product_key int, foreign key(product_key) references Product(product_key));

insert into Product values(5),(6);
insert into Customer values(1,5),(2,6),(3,5),(3,6),(1,6);

select * from Product;
select * from Customer;

-- Write an SQL query for a report that provides the customer ids from the Customer table that bought all the products in the Product table.

-- Return the result table in any order.

select customer_id from Customer group by customer_id having count(distinct product_key)=(select count(*) from Product);

SELECT DISTINCT c1.customer_id 
FROM Customer c1 
JOIN Product p ON c1.product_key = p.product_key 
LEFT JOIN Customer c2 ON c1.customer_id = c2.customer_id AND c2.product_key != p.product_key 
GROUP BY c1.customer_id 
HAVING COUNT(c2.product_key) = COUNT(p.product_key);


-- Table: Products

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
-- product_id is the primary key for this table.
-- low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
-- recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.


-- Write an SQL query to find the ids of products that are both low fat and recyclable.

create table Products( product_id int,low_facts enum('Y','N'),recyclable enum('Y','N'));

insert into Products values(0,'Y','N'),(1,'Y','Y'),(2,'N','Y'),(3,'Y','Y'),(4,'N','N');

select product_id from Products where low_facts='Y' and recyclable='Y';

-- 3.Problem statement
--  A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.

--  However, this assignment is very heavy because there are hundreds of records to calculate.

-- Could you help Tim by writing a query to judge whether these three  sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.

-- | x  | y  | z  |
-- |----|----|----|
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |

--  For the sample data above, your query should return the follow result:
--  | x  | y  | z  | triangle |
--  |----|----|----|----------|
--  | 13 | 15 | 30 | No       |
--  | 10 | 20 | 15 | Yes      |

create table triangle (x int, y int, z int);

insert into triangle values(13,15,30),(10,20,15);
select  x,y,z,  case when x+y>z and y+z>x and x+z>y then "yes" else "no" end as TRIANGLE from triangle;

-- 4.Problem statement
-- Table: Friends

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- | activity      | varchar |
-- +---------------+---------+
-- id is the id of the friend and primary key for this table.
-- name is the name of the friend.
-- activity is the name of the activity which the friend takes part in.
-- Table: Activities

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- +---------------+---------+
-- id is the primary key for this table.
-- name is the name of the activity.

create table Friends(id int,name varchar(100),activity varchar(100) ,primary key(id));
create table Activities(id int,name varchar(100),primary key(id));

insert into Friends values(1,"Jonathan D.",'Eating'),(2,"Jade W.",'Singing'),(3,"Victor J.",'Singing'),(4,'Elvis Q.','Eating '),(5,'Daniel A.','Eating '),(6,'Bob B.','Horse Riding');
insert into Activities values(1,'Eating'),(2,'Singing'),(3,'Horse Riding');

select * from Friends;
select * from Activities;

WITH Activity_Participant_Counts AS (
    SELECT 
        activity,
        COUNT(DISTINCT id) AS participant_count 
    FROM Friends 
    GROUP BY activity
), 
MinMaxCounts AS (
    SELECT 
        MAX(participant_count) AS max_count,
        MIN(participant_count) AS min_count 
    FROM Activity_Participant_Counts
) 
SELECT 
    activity 
FROM 
    Activity_Participant_Counts 
CROSS JOIN 
    MinMaxCounts 
WHERE 
    Activity_Participant_Counts.participant_count NOT IN (max_count, min_count);
    
 --    5.Problem statement
-- There is a table courses with columns: student and class

-- Please list out all classes which have more than or equal to 5 students.

-- For example, the table:

-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+

-- Should output:

-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+

create table student(student varchar(2),class varchar(100));
insert into student values('A','Math'),('B','English'),('C','Math'),('D','Biology'),('E','Math'),('F','Computer'),('G','Math'),('H','Math'),('I','Math');

select class from student group by class having count(distinct student)>=5;

-- 6.Problem statement
-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+

create table Person(Id int,Email varchar(100));
insert into Person values(1,'a@b.com'),(2,'c@d.com'),(3,'a@b.com');

select Email from Person group by Email having count(Email)>1;

-- 7.Problem statement
-- Table: Submissions

-- +---------------+----------+
-- | Column Name   | Type     |
-- +---------------+----------+
-- | sub_id        | int      |
-- | parent_id     | int      |
-- +---------------+----------+
-- There is no primary key for this table, it may have duplicate rows.
-- Each row can be a post or comment on the post.
-- parent_id is null for posts.
-- parent_id for comments is sub_id for another post in the table.


-- Write an SQL query to find number of comments per each post.

-- Result table should contain post_id and its corresponding number_of_comments, and must be sorted by post_id in ascending order.

-- Submissions may contain duplicate comments. You should count the number of unique comments per post.

-- Submissions may contain duplicate posts. You should treat them as one post.

-- The query result format is in the following example:

-- Submissions table:
-- +---------+------------+
-- | sub_id  | parent_id  |
-- +---------+------------+
-- | 1       | Null       |
-- | 2       | Null       |
-- | 1       | Null       |
-- | 12      | Null       |
-- | 3       | 1          |
-- | 5       | 2          |
-- | 3       | 1          |
-- | 4       | 1          |
-- | 9       | 1          |
-- | 10      | 2          |
-- | 6       | 7          |
-- +---------+------------+

--  Result table:
-- +---------+--------------------+
-- | post_id | number_of_comments |
-- +---------+--------------------+
-- | 1       | 3                  |
-- | 2       | 2                  |
-- | 12      | 0                  |
-- +---------+--------------------+

-- The post with id 1 has three comments in the table with id 3, 4 and 9. The comment with id 3 is repeated in the table, we counted it only once.
-- The post with id 2 has two comments in the table with id 5 and 10.
-- The post with id 12 has no comments in the table.
-- The comment with id 6 is a comment on a deleted post with id 7 so we ignored it.

create table submissions(sub_id int,parent_id int);
insert into submissions values(1,null),(2,null),(1,null),(12,null),(3,1),(5,2),(3,1),(4,1),(9,1),(10,2),(6,7);
select * from submissions;

select s.sub_id as post_id,count(distinct c.sub_id) as number_of_comments from submissions s left join submissions c on s.sub_id=c.parent_id where s.parent_id 
is null group by s.sub_id order by s.sub_id;