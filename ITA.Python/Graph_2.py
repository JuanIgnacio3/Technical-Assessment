import os
import sqlite3
import pandas
import matplotlib.pyplot as mp

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "..", "ITA.DataBase", "db.db")

conn = sqlite3.connect(DB)

query = """
SELECT
	Platform,
	round(100.0 * sum(Global_Sales) /
		 (SELECT sum(Global_Sales) FROM videogames WHERE Year = 2015), 2) AS MarketShare
FROM videogames
WHERE Year = 2015
GROUP BY Platform
ORDER BY MarketShare DESC;
"""

rd = pandas.read_sql(query, conn)
conn.close()

platforms = rd["Platform"].tolist()
percentages = rd["MarketShare"].tolist()

mp.figure(figsize=(10,4))

mp.bar(platforms, percentages)

mp.xlabel("Platform")
mp.ylabel("Marker Share (%)")
mp.title("Market Share by Platform 2015")
mp.ylim(0.100)
mp.xticks(rotation=45, ha="right")

for i, value in enumerate(percentages):
    mp.text(i, value + 1, f"{value}%", ha="center", fontsize=9)

mp.tight_layout()
mp.show()
