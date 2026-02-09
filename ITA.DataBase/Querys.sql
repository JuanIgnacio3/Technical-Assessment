
--Table ESRB to ratings games by age
CREATE TABLE ESRB (
	ID INTEGER PRIMARY KEY,
	Rating TEXT NOT NULL,
	AgeMin INTEGER NOT NULL
);

--Insert on ESRB rated based on genre
INSERT OR replace INTO ESRB (ID, Rating, AgeMin)
SELECT
	Rank,
	CASE
		WHEN Genre IN ('Shooter', 'Action') THEN 'M'
		WHEN Genre IN ('Sports', 'Racing') THEN 'E'
		WHEN Genre = 'Roley-Playing' THEN 'M'
		ELSE 'E10+'
	END AS Rating,
	CASE
		WHEN Genre IN ('Shooter', 'Action') THEN 17
		WHEN Genre IN ('Sports', 'Racing') THEN 0
		WHEN Genre = 'Roley-Playing' THEN 13
		ELSE 10
	END AS AgeMin
FROM videogames
WHERE Rank <= 1000;



--Regional Sales Distribution, graph of Wii Sports 2006
SELECT
	v.Name,
	v.Platform,
	v.Year,
	round(100.0 * v.NA_Sales / nullif(v.Global_Sales, 0), 2) AS "NA %",
	round(100.0 * v.EU_Sales / nullif(v.Global_Sales, 0), 2) AS "EU %",
	round(100.0 * v.JP_Sales / nullif(v.Global_Sales, 0), 2) AS "JP %",
	round(100.0 * v.Other_Sales / nullif(v.Global_Sales, 0), 2) AS "Other %"
FROM videogames v
WHERE v.Rank <=50;



--Platform market share by year
SELECT
	Platform,
	round(100.0 * sum(Global_Sales) /
		 (SELECT sum(Global_Sales) FROM videogames WHERE Year = 2015), 2) AS "2015 %"
FROM videogames
WHERE Year = 2015
GROUP BY Platform
ORDER BY "2015 %" DESC;



--Regional Sales Distribution by ESRB rating
SELECT
	e.Rating,
	round(100.0 * sum(v.NA_Sales)/ sum(v.Global_Sales), 2) AS NA,
	round(100.0 * sum(v.EU_Sales)/ sum(v.Global_Sales), 2) AS EU,
	round(100.0 * sum(v.JP_Sales)/ sum(v.Global_Sales), 2) AS JP,
	round(100.0 * sum(v.Other_Sales)/ sum(v.Global_Sales), 2) AS Other
FROM videogames v
JOIN ESRB e ON v.Rank = e.ID
GROUP BY e.Rating;


--Platforms that depends of adult games
SELECT
	v.Platform,
	round(sum(v.Global_Sales), 2) AS RatedSales
FROM videogames v
JOIN ESRB e ON v.Rank = e.ID
WHERE e.Rating = 'M'
GROUP BY v.Platform
ORDER BY RatedSales DESC;