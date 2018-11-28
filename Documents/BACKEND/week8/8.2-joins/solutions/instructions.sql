-- All of the challenges are solved here in comments.

-- Challenge 2

-- 
-- List of relations
-- Schema |          Name          |   Type   |     Owner      
-- --------+------------------------+----------+----------------
-- public | cities                 | table    | nujpfwggqgeirz
-- public | cities_id_seq          | sequence | nujpfwggqgeirz
-- public | company_records        | table    | nujpfwggqgeirz
-- public | company_records_id_seq | sequence | nujpfwggqgeirz
-- public | states                 | table    | nujpfwggqgeirz




-- Challenge 3

-- Get all data from states
SELECT * FROM states;

-- Get higher population states (greater than 3 million)
SELECT * FROM states WHERE population > 3000000;

-- Get higher population cities (greater than 1 million)
SELECT * FROM cities WHERE population > 1000000;

-- Get all cities named Phoenix
SELECT * FROM cities WHERE name = 'Phoenix';

-- Get all cities within a bounding box around the Bay Area.
SELECT * FROM cities WHERE latitude > 37.20 AND latitude < 38.19 AND
longitude > -122.67 AND longitude < -121.72;

-- Get all the companies that raised more than 100m
SELECT * FROM company_records WHERE raised_amount > 100000000;


-- Challenge 4:
SELECT company_records.name, company_records.raised_amount,
       states.name, states.population
FROM company_records
INNER JOIN states ON company_records.state_id = states.id; 


-- Challenge 5:

EXPLAIN ANALYZE SELECT * FROM cities WHERE name = 'Graham';
--------------------------------------------------------------------------------------------------
-- Seq Scan on cities  (cost=0.00..38.30 rows=1 width=34) (actual time=0.272..0.407 rows=2 loops=1)
--    Filter: ((name)::text = 'Graham'::text)
--    Rows Removed by Filter: 3226
-- Planning time: 0.228 ms
-- Execution time: 0.429 ms
-- (5 rows)

-- This means that it took ~0.6 ms total to run, and that it did a
-- "sequential scan" to find the necessary data






-- Challenge 6:

CREATE INDEX name_index ON cities (name);

EXPLAIN ANALYZE SELECT * FROM cities WHERE name = 'Graham';
-- Index Scan using name_index on cities  (cost=0.06..4.06 rows=1 width=34) (actual time=0.029..0.036 rows=2 loops=1)
-- Index Cond: ((name)::text = 'Graham'::text)
-- Planning time: 0.130 ms
-- Execution time: 0.074 ms
-- (4 rows)


-- Challenge 7 (Bonus)

-- Seq scan is linear
-- Index is using a "B-Tree" which permits binary search


-- Advanced Challenge

-- 1. ~0.5 second

-- 2. ~2000 users or queries per second (at most, just solely based on this)

-- 3. In real life, the datasets are usually larger and more complex, which
-- means for 300,000 items in the database it would fully crash the system with
-- only 20 simultaneous users

