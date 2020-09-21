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

# Question - 2
<br />
The mentioned architecture model is a basic web application model. 
<br />
The CDN is used to deliver the content to end-users(clients) to reduce the latency and reduce the load on application servers. 
Then for requests that are not cached by the CDN, they are processed by the Load Balancer which distributes the traffic among the application servers. The aplication servers then send responses to the client.
<br />


## Benefits:

<br />
The use of CDN will reduce the latency of the responses of the contents that can be cached. We used Akamai CDN in our previos ecommerce project.
<br />
The use of Load balancer will help handling the application server failures and will also give an increased scalability. 
<br />
The use of two load balancers is also to handle failures and increase the availability of the application.
<br />
When a load balancer goes down the other load balancer can handle all the traffic until the failed one is restored.
 
 <br />
 
 ## How do you roll out an update to the service without any downtime impact to the app foo.com
 
 <br />
 First I would make sure to do this activity on a day/time when less customer traffic is expected. Then, will route all the traffic to one service using the CDN. 
 <br />
 Now, I can roll an update to the service that is not taking any traffic. After the update is completed I will start moving the traffic from 5% and increase it to 100 if everything is stable.
 <br />
 Once all the traffic is moved to the service that has the new update, I will update the other service and then again move the traffic between services 50-50 if no issues are found. 
 <br />
 This way we have one service always to serve the customers without downtime.
 <br />
 
 
 ## If you have to deploy this App to the Cloud what services would you use and explain the Architecture.
 
 
 <br />
 AWS:
 If I have to deploy this in cloud this would me my architecture.
 <br />
 Route 53 ---------> Elastic load balancer's (in multiple regions) ------------> EC2 instances in an Auto scaling group spread across multiple AZ. For CDN I will use aws CloudFront. 
 <br />
 Here, Route 53 is a DNS service that performs global server load balancing by routing each request to the AWS region closest to the client's location. 
 <br />
 Then the elastic load balancer balances the traffic between EC2 instances in different availability zones.
 <br />
 Finally the auto scaling group will size up and size down the instance based on the load to the instances.
 <br />
 CloudFront will be acting like CDN which caches the content on edge locations and provides the content to end-users with low latency.

# Question - 3
<br />
I did not properly understand what Ascending / Descending means in terms of filenames as it was not mentioned how the file naming convention is, so I just assumed it to be the last update for the file. i.e. the last updated file comes first in the order of execution. 
<br />
But, if the files here are the same as in the first question like 01-test.sql, I will use filename[0:2] to get the first two characters of the files and order them accordingly.
<br />
Also, I tested this is my local machine and I choose the home directory to be "D:"
<br />
Improvements - I need to reduce the code duplicacy by using functions. 
