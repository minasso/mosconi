###Mosconi Cup Web Scraping/Data Munging/Statistical Analysis

This is a web scraping/data analysis project on the Mosconi Cup data from 1994 to 2016.

The Mosconi Cup is an annual event in the game of pocket billiards whereby the best players in America face off against the best players in Europe. Over time, the game of pool has lost a lot of its prowess and, as such, it is hard to find good statistical information on the players' past performances throughout the years. This project is an attempt to remedy that by providing the fans with interesting and useful stats regarding the players' past performances in the sport's most entertaining annual tournament.

##Web Scraping/Data Munging

The first step involved scraping wikipedia for results data. The format changed in 1998, so I started working with the newer data from 1998 to 2016.

The first hurdle I encoutered was when I noticed that there was no data from 2014. I scoured the web and found results data on the matchroom sports website.

The next difficulty occurred when I noticed that my data was still slightly off from expected values (when compared to data compiled by a user on the AZ billiards forum as well as the official mosconi cup facebook page). I quickly discovered that only recent data was off and visually inspected the wikipedia pages to find that the 2015 data was presented backwards (all other years had European players listed first in the wiki table). Once I discovered this problem, it was a relatively easy fix to adjust my regular expression and properly capture the data. (In retrospect, maybe I could have just switched the column names and positions?)

Next, I decided that I may want to index the data by year, and so I had to rescrape the data, this time using multiindexing. 

After this, I made a new regular expression object to capture data from 1994-1998. At this point, I had the data from all the years (including the years as multiindex), but I was still unable to do any analysis on the 'teams' matches, since the players' names were not included.

My next fix involved inserting the players' names into the correct places on the team matches for each year, allowing analysis on team matches as well as a true 'total' for matches won, etc.
