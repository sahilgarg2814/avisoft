create database 12_march_2024;

use 12_march_2024;

create table salary(ID int,Salary int, primary key(ID));

insert into salary (ID,Salary) values (1,100),(2,200),(3,300);

select * from salary;

-- Write a SQL query to get the second highest salary from the 
-- Employee table.

select Salary as Second_highest_salry from salary order by Salary desc limit 1 offset 1;


-- 2.Table: Calls

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | from_id     | int     |
-- | to_id       | int     |
-- | duration    | int     |
-- +-------------+---------+
-- This table does not have a primary key, it may contain duplicates.
-- This table contains the duration of a phone call between from_id and to_id.
-- from_id != to_id


-- Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

-- Return the result table in any order.

-- The query result format is in the following example:



-- Calls table:
-- +---------+-------+----------+
-- | from_id | to_id | duration |
-- +---------+-------+----------+
-- | 1       | 2     | 59       |
-- | 2       | 1     | 11       |
-- | 1       | 3     | 20       |
-- | 3       | 4     | 100      |
-- | 3       | 4     | 200      |
-- | 3       | 4     | 200      |
-- | 4       | 3     | 499      |
-- +---------+-------+----------+

create table Calls(from_id int,to_id int,duration int);

insert into Calls values (1,2,59),(2,1,11),(1,3,20),(3,4,100),(3,4,200),(3,4,200),(4,3,499);

select * from Calls;

select least(from_id,to_id) as person1,
       greatest(from_id,to_id) as person2,
       count(*) as call_count,
       sum(duration) as total_duration
from calls
group by least(from_id,to_id),greatest(from_id,to_id);

select case when from_id < to_id then from_id else to_id end as person1,
       case when from_id < to_id then to_id else from_id end as person2,
       count(*) as call_count,
       sum(duration) as total_duration
	from Calls
    group by person1,person2
    order by person1,person2;
       
       


-- 3.A U.S graduate school has students from Asia, Europe and America. The students' location information are stored in table student as below.


-- | name   | continent |
-- |--------|-----------|
-- | Jack   | America   |
-- | Pascal | Europe    |
-- | Xi     | Asia      |
-- | Jane   | America   |


-- Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. 
-- The output headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.

create table student1 (name varchar(200),continent varchar(200));
insert into student1 values ('Jack','America'),('Pascal','Europe'),('Xi','Asia'),('Jane','America');

select 
max(case when continent='America' then name end) as America,
max(case when continent='Asia' then name end) as Asia,
max(case when continent='Europe' then name end) as Europe
from 
(SELECT
        name,
        continent,
        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS row_num
    FROM
        student1
        ) as sorted_student
group by
row_num;