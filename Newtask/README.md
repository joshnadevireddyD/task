Retrieving Rotten Tomatoes Rating From OMBD API

Objective
The objective of this Project is to display the Rotten Tomatoes rating for particular movie name using Programming.
Introduction
The Project is to display the Rotten Tomatoes rating details of the particular movie ,when we enter the movie name,it should fetch the details of that movie from the OMDB database using this python Programming.
Pre-requisites
Python,Docker
Procedure
Step 1: Open command line interface terminal
step 2: Now try to create image and container by running the Dockerfile
step 3: To create image execute the below command
docker build -t data .
step 4: To create container execute the below command
docker run -ti data
Example:
Enter the Movie name: 300 
Rotten Tomatoes Rating is "60%"

