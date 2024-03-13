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
create table Activities(id
