# Internship Technical Assessment

## Overview

This project analyzes historical video game sales data using SQL and
Python to extract meaningful business insights. The context used for 
this interpretation is that of a multinational company that sells 
video games in all regions, so the analysis focuses on how to ensure 
the company maintains its metrics and can use historical video game 
data to increase sales.

------------------------------------------------------------------------

## Dataset

Source: Kaggle Video Game Sales Dataset\
Link: https://www.kaggle.com/datasets/gregorut/videogamesales

The dataset includes:

-   Game Name\
-   Platform\
-   Release Year\
-   Genre\
-   Publisher\
-   Regional Sales (NA, EU, JP, Other)\
-   Global Sales

------------------------------------------------------------------------

## Technologies Used

-   Python\
-   Pandas\
-   SQLite\
-   SQL\
-   Matplotlib

------------------------------------------------------------------------

## Installation

Install required Python libraries:

py -m pip install pandas
py -m pip install matplotlib

------------------------------------------------------------------------

## Database Setup

The CSV dataset is imported into SQLite using Python and Pandas.

Database location:

    ITA/ITA.DataBase/db.db

------------------------------------------------------------------------

## How To Run

### 1. Import Dataset into SQLite

py ITA.DataBase/SQLite.py

This script: - Reads the CSV file\
- Creates the SQLite database\
- Creates the videogames table automatically

------------------------------------------------------------------------

### 2. Run Graph Visualizations

Example:

py ITA.Python/Graph_2.py

Graphs are generated dynamically using SQL queries executed through
Python.

------------------------------------------------------------------------

## Additional Data Enrichment

An additional table called **ESRB** was created to simulate age rating
segmentation.

### ESRB Table Structure

  Column   Description
  -------- -------------------------
  ID       Matches videogames.Rank
  Rating   ESRB rating category
  AgeMin   Minimum recommended age

### Purpose

Allows demographic analysis such as:

-   Adult vs family game sales performance\
-   Regional demographic preferences\
-   Platform audience segmentation

------------------------------------------------------------------------

## SQL Analysis

### Regional Sales Distribution

Shows how global sales are distributed geographically per game.

------------------------------------------------------------------------

### Platform Market Share by Year

Identifies dominant platforms in specific years.

------------------------------------------------------------------------

### Regional Preferences by ESRB Rating

Shows how different age segments perform across regions.

------------------------------------------------------------------------

### Mature Content Dependency by Platform

Identifies platforms strongly associated with mature-rated games.

------------------------------------------------------------------------

## Python Extension

Python is used to:

-   Connect to SQLite database\
-   Execute SQL queries\
-   Transform results into graph-ready datasets\
-   Generate visualizations using Matplotlib

Example connection:

conn = sqlite3.connect(DB)
df = pandas.read_sql(query, conn)
conn.close()

------------------------------------------------------------------------

## Business Value

This analysis demonstrates how raw sales data can support business
decisions such as:

-   Market expansion strategies\
-   Platform targeting\
-   Demographic content planning\
-   Regional marketing optimization

------------------------------------------------------------------------

### By Juan Ignacio Vargas Ramírez
