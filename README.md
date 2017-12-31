## Mosconi Cup Web Scraping/Data Cleaning/Statistical Analysis

This is a web scraping and data analysis project on the Mosconi Cup data from 1994 to 2016.

The Mosconi Cup is a yearly pocket billiards event during which the best players in America face off against the best players in Europe in a team 9-ball tournament. Over the last few decades, the game of pool has lost a lot of its following, and thus it has become hard to find good statistical information on the players' past performances. This project is an attempt to remedy that by providing the fans with interesting and useful stats on the sport's most entertaining annual tournament.

### 1- Web Scraping and Temporary Storage

Twenty-four years worth of Mosconi Cup match results data was scraped from Wikipedia using Python with the help of several 3rd party libraries (requests, BeautifulSoup, regular expressions, etc.)

Initial scrape only got data from 1998 to 2013.

2014 data was missing on Wikipedia and had to be acquired from a different source (Matchroom Sports website)

2015 data was backwards relative to other data so scraper had to be tweaked a bit.

1994-1998 data was of a different format and had to be scraped separately then integrated into the main data set.

### 2- Data Cleaning and Organization

The data cleaning process involved several steps, including fixing encoding errors and misspellings, purging unnecessary data, and writing several functions to either improve the appearance of the data, or extract features as new columns in the dataframe.

The cleaned data was then stored in a sql database in the 'results' table.

Player data was acquired seperately and stored in 'players' table. 

In addition, the 'Yearly' table was created to store each year's final score, along with location. 'MVP' data was extracted from the yearly data and stored in the 'mvp' table.

### 3- Data Analysis

At the start of the analysis, functions were created to mine the match level results data using boolean indexing. These efforts eventually led to the creation of the 'playerstats' table in which each individual player's stats have been aggregated from the match level results.

### 3-2 In Depth Player Performance Analysis

This section uses an object oriented approach to provide an in-depth analysis into individual players' past performances. Topics explored include: singles vs. doubles, home vs. away, singles analysis by opponent, doubles analysis by partner, yearly performance trends, and more.