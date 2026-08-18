# i learn sql crud commands like where, delete, update, and select , and some interview techinical questions
enlish learing practive one day completely on interview, i will continue tomaorrow as well
a little busy day, so dont done much, just overview

# Find the movie with a row id of 6

SELECT * FROM movies 
WHERE id = 6;

#Find the movies released in the years between 2000 and 2010

SELECT * FROM movies 
WHERE year BETWEEN 2000 AND 2010;

(Alternatively, you can use WHERE year >= 2000 AND year <= 2010;)

#3. Find the movies not released in the years between 2000 and 2010

SELECT * FROM movies 
WHERE year NOT BETWEEN 2000 AND 2010;
(Alternatively, you can use WHERE year < 2000 OR year > 2010;)

#4. Find the first 5 Pixar movies and their release year
SELECT title, year FROM movies 
LIMIT 5;




Task 1: List all the Canadian cities and their populations

SELECT name, population FROM cities WHERE country = 'Canada';

Task 2: Order all the cities in the United States by their latitude from north to south

SELECT * FROM cities WHERE country = 'United States' ORDER BY latitude DESC;

#Note: North to south means starting with the highest positive latitude value and moving down.

#Task 3: List all the cities west of Chicago, ordered from west to east
 
SELECT name FROM cities WHERE longitude < (SELECT longitude FROM cities WHERE name = 'Chicago') ORDER BY longitude ASC;

#Note: Western longitudes have lower values (or more negative numbers in the Western Hemisphere). Sorting ASC orders them from the furthest west to the closest east toward Chicago.

# Task 4: List the two largest cities in Mexico (by population)
#
SELECT name, population FROM cities WHERE country = 'Mexico' ORDER BY population DESC LIMIT 2;

Task 5: List the third and fourth largest cities (by population) in the United States and their population

SELECT name, population FROM cities WHERE country = 'United States' ORDER BY population DESC LIMIT 2 OFFSET 2;