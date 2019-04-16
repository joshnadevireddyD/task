Retriving Rotten Tomatoes rating fropm OMBD API key
   
Objective
The objective of this documentation is to display the Rotten Tomatoes rating for particular movie name using Programming.

Introduction

The script is to display the entire details of the particular movie , which we have entered when we run that script,should fetch the details of that movie from the database using this python script

Pre-requisites

Python Installed


Procedure

Step 1: Open command line interface treminal

step 2: Make sure that source code and Dockerfile should be present in one folder

step 3: Start the service of docker 

         service docker start

step 4: Now try to create image and container by running the Dockerfile

step 5: To create image execute the below command
        
        docker build -t data .

step 6: To create container execute the below command
        
        docker run -ti -p 8001:8001 data /bin/bash

Example: 

Enter the Movie name:
Aquaman
Rotten Tomatoes Rating is "8%" 

