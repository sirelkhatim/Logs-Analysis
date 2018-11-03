# Logs-Analysis

## Motivation

In this project we will use python and SQL to summarize information about the news dataset. These are the three questions that I will answer in this project
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Libraries requred

1. python 3.6
2. pyscopg2 2.7.5
3. PostgresSQL 9.5.10

In addition to this you will need vagrant (https://www.vagrantup.com/) and virtualbox (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to set up a virtual environment to run linux on and the SQL server. I also used Git bash for my terminal since I am using Windows. If you are using linux, you should be fine

## Files
- news.py: the code to run in the environment to get the results of the three questions
- output.txt: Example output of my code

## How to run news.py
After having installed vagrant and virtual box. You need to open a terminal bash and move into the virtual box that you have installed. You then have to move your terminal into the folder vagrant. (Note: you should have put news.py into the vagrant folder) Then type "vagrant up" and then "vagrant ssh" and finally "python news.py" and you should see the same output as output.txt


