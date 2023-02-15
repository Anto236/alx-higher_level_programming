-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
