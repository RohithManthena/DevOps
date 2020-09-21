# DevOps

# Question - 1
<br />
I completed this question using an AWS Linux machine.
<br />
I have opened the 1433 port for my ipaddress by configuring the AWS security groups and I was able to connect from my SSMS and verify the things done.
<br />
The thing I did not implement in this quesiton is that of running all the sql scripts in the DBscripts folder. I ran all the files individually using commands.
<br />
To implement that my idea is to get all the file names first and then get the first two characters of all the filenames change them to int type and then execute them in increasing order. I am very comfortable in implementing this using python but I got some failures while trying it with shell. But I can do this given time.
<br />


# Question - 3
<br />
I did not properly understand what Ascending / Descending means in terms of filenames as it was not mentioned how the file naming convention is, so I just assumed it to be the last update for the file. i.e. the last updated file comes first in the order of execution. 
<br />
But, if the files here are the same as in the first question like 01-test.sql, I will use filename[0:2] to get the first two characters of the files and order them accordingly.
<br />
Also, I tested this is my local machine and I choose the home directory to be "D:"
<br />
Improvements - I need to reduce the code duplicacy by using functions. 
