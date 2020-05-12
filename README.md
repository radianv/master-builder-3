# Master Builder 3

## AWS Services
With Amazon Web Services (AWS), you can provision compute power, storage and other resources, gaining access to a suite of elastic IT infrastructure services as your business demands them. With minimal cost and effort, you can move your application to the AWS cloud and reduce capital expenses, minimize support and administrative costs, and retain the performance, security, and reliability requirements your business demands.

## The Web Base application
A simple CRUD application using Flask and MySQL. This project has been based  on [this example](https://github.com/muhammadhanif/crud-application-using-flask-and-mysql), this Application is
docker based, the main objective of this project is elevate this Monolith to Microservices, in order to achieve it 
we will install a **Core Web Application** from next examples with just a bit modification,  we have three options:

   - Using local based install, please see [Here](topics/my_local_monolith_install.md)
   
   - If you are familiar with docker you can use my docker approach, please see [Here](docker_approach/my_docker_monolith_install.md)
   
   - Finally, Web Application with Microservices (__*this case is recommended it's has good fit about the initial use case*__), please see [Here](workspace/dev/code-webapp-micro/frontend/)
        
    
# Migrating your Existing Applications to the AWS Cloud

The strategy is using __"Forklift Migration Strategy"__, we will convert current approach from Monolithic to Microservices Application next steps below:

## Objectives of this solution
- Workload web application to AWS cloud.
- Its purpose is to decouple and modularise system services
- Leverage cloud
- Allow for horizontal scalability
- Separate the system concerns (Microservices)
- Isolated and decoupled deployments
- Allow for continuous delivery
- Allow for horizontal scalability
- Service can be scaled Independently
 

## The Strategy

   1. Rehosting & Replatforming , lift-tinker-and-shift.
   2. Refactoring / Re-architecting

## Rehosting & Replatforming , lift-tinker-and-shift.

![Monolithic Application to AWS Cloud][img1]

### Activities

Step 1, Creating and Setup EC2 Instance for initial environment.

- Go to [Lunch instance wizard](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:)
- Chose Free tier and select, **Amazon Linux 2 AMI (HVM), SSD Volume Type**.
. For instance type we will use **t2.large** it has well fit for Web Application Environment performance, please see more about [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- For ** Configure Instance Details** we will setup next Bootstrap script, for more information see [Running commands on your Linux instance at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
```
#!/bin/bash
yum update -y
yum install -y git
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
git clone https://github.com/radianv/master-builder-3.git
docker-compose -f /master-builder-3/workspace/dev/code-webapp-micro/frontend/docker-compose.deploy.yml up -d
```
- Add Storage as is (just default).
- Add Tags, use next values: `key=Name` and `Value=WebServer1`
- Next Configure New Security Group, next values: 
  - Name: webMB3
  - VPC: default
  - Security group rules: Allow access to next ports: `80`, `22`, `3306`  
- Finally Review and Launch

Step 2, Create ELB and Target Groups.

Step 3, Add WebServer to Target Group.

Step 4, check  the application is a Live on AWS:http://myalb-1820198848.us-east-1.elb.amazonaws.com/

## Refactoring / Re-architecting

![Monolithic Application to Microservices][img2]

### Activities

Step 1, Move the application to Microservices using ECS.

Step 2, Containerize the Monolith

Step 3, Deploy the Monolith

Step 4. Break the Monolith

step 5. Deploy Microservices

[img0]: images/mb3-monolithic-app.png "Monolithic Application"
[img1]: images/mb3-monolithic_app-to-cloud.png "Monolithic Application to Cloud"
[img2]: images/mb3-microservices-app.png "Microservices Application"

