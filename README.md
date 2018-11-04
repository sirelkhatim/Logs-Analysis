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
4. newdata.zip: zip file that contains the news SQL table
5. vagrantfile: vagrant file used to setup the environment

In addition to this you will need vagrant (https://www.vagrantup.com/) and virtualbox (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to set up a virtual environment to run linux on and the SQL server. I also used Git bash for my terminal since I am using Windows. If you are using linux, you should be fine

## Files
- news.py: the code to run in the environment to get the results of the three questions
- output.txt: Example output of my code

## How to run news.py
1. Install vagrant and virtualbox from the links provided above
2. Download newsdata.zip and unzip it in the vagrant folder in your Virtual environment folder
3. Download the vagrantfile and news.py and put it in the vagrant folder in your virtual environment folder
4. You need to open a terminal bash and move into the virtual box that you have installed. You then have to move your terminal into the folder vagrant. For example "cd ~/home/FSND_virtual/vagrant/"
5. Then type "vagrant up" to initialize the repository 
6. Then type "vagrant ssh" and 
8. To load the database type: psql -d news -f newsdata.sql
7. Finally type: "python news.py". You should see the same output as output.txt


