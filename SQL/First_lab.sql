
/*1.Created a Table named as Countries and added values to it
 
CREATE TABLE Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255),
);

-- insert
INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');

-- fetch 
SELECT * FROM Countries;
/*-----------------------------------------------------------------------------------------------------
/*2.Duplicating an existing Table
-- creating table

CREATE TABLE Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255)
);

-- insert
INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');

-- Drop Dup_Countries if it already exists
DROP TABLE IF EXISTS Dup_Countries;

-- Create the Dup_Countries table
CREATE TABLE Dup_Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255)
);

-- Insert data from Countries into Dup_Countries
INSERT INTO Dup_Countries(Country_id, Country_name, Country_region)
SELECT Country_id, Country_name, Country_region
FROM Countries;

--- adding not null constrain to existing table
ALTER Countries
MODIFY COLUMN Country_id INTO NOT

-- Fetch data from Dup_Countries
SELECT * FROM Dup_Countries;
/*-----------------------------------------------------------------------------------------------------
/* 3.Add Multiple values into Table 

-- create
CREATE TABLE Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255)
);

-- insert
INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');

-- fetch 
SELECT * FROM Countries;
/*-----------------------------------------------------------------------------------------------------
/* 4. Create a table and add single value at time

CREATE TABLE Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255)
);

INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');

-- insert a single value at a time in table
INSERT INTO Countries
VALUES (005,'Ghana','Africa');

SELECT * FROM Countries;

/*-----------------------------------------------------------------------------------------------------
/*5. Inserting new row using 'unique constraint'
-- create
CREATE TABLE Countries (
  Country_id int NOT NULL,
  Country_name varchar(255),
  Country_region varchar(255)
);

-- insert
INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');


-- fetch 
INSERT INTO Countries
VALUES (005,'Ghana','Africa');

ALTER TABLE Countries 
ADD CONSTRAINT unique_country_region UNIQUE (Country_id, Country_region);

INSERT IGNORE INTO Countries (Country_id, Country_name, Country_region) 
VALUES (005, 'Germany', 'Europe');

-- Fetch data from Dup_Countries
SELECT * FROM Countries;
/*-----------------------------------------------------------------------------------------------------
/*6.Not Null Constraint
CREATE TABLE Countries (
  Country_id int,
  Country_name varchar(255),
  Country_region varchar(255)
);

-- insert
INSERT INTO Countries(Country_id,Country_name,Country_region) 
VALUES 
(001,'India','Asia'),
(002,'Sweden','Europe'),
(003,'Japan','Asia'),
(004,'Spain','Europe');


-- fetch 
INSERT INTO Countries
VALUES (005,'Ghana','Africa');

ALTER TABLE Countries 
ADD CONSTRAINT unique_country_region UNIQUE (Country_id, Country_region);

INSERT IGNORE INTO Countries (Country_id, Country_name, Country_region) 
VALUES (005, 'Germany', 'Europe');

-- Fetch data from Dup_Countries
SELECT * FROM Countries;
/*_____________________________________________________________________________________________________