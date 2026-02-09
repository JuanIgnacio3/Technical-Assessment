import os
import sqlite3
import pandas   

BASE = os.path.dirname(os.path.abspath(__file__))

CSV = os.path.join(BASE, "vgsales.csv")
DB = os.path.join(BASE, "db.db")

rd = pandas.read_csv(CSV)

conn = sqlite3.connect(DB)
rd.to_sql("videogames", conn, if_exists="replace", index=False)
conn.close()

print("running...")
