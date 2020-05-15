# Master Builder 3

## AWS Services
With [Amazon Web Services (AWS)](https://aws.amazon.com/what-is-aws/), you can provision compute power, storage and other resources, gaining access to a suite of elastic IT infrastructure services as your business demands them. With minimal cost and effort, you can move your application to the AWS cloud and reduce capital expenses, minimize support and administrative costs, and retain the performance, security, and reliability requirements your business demands.

## The Web Base application
A simple **Web Application using Flask and MySQL**. This project has been based  on [CRUD application using Flask and MySQL](https://github.com/muhammadhanif/crud-application-using-flask-and-mysql) and 
this [Hands on Microservices with Python](https://github.com/PacktPublishing/Hands-on-Microservices-with-Python), 
this Application is docker based, the main objective of this project is elevate this Monolith to Microservices on AWS, 
in order to achieve it we will install a **Core Web Application** from next examples with just a bit modification,  
we have three options (we will use **C** Option):

   - A, Using local based install, please see [Here](topics/my_local_monolith_install.md)
   
   - B, If you are familiar with docker you can use my docker approach, please see [Here](docker_approach/my_docker_monolith_install.md)
   
   - C, Finally, Web Application with Microservices (__*this case is recommended it's has good fit about the initial use case*__), please see [Here](workspace/dev/code-webapp-micro/frontend/)
        
    
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

__Step 1.__ Creating and Setup EC2 Instance for initial environment.

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
chkconfig docker on
```
- Add Storage as is (just default).
- Add Tags, use next values: `key=Name` and `Value=WebServer1`
- Next Configure New Security Group, next values: 
  - Name: webMB3
  - VPC: default
  - Security group rules: Allow access to next ports: `80`, `22`, `3306`  
- Finally Review and Launch

__Step 2.__ Create ELB and Target Groups.
  - **_under construction_**

__Step 3.__ Add WebServer to Target Group.
  - **_under construction_**

__Step 4.__ check  the application is a Live on AWS:http://myalb-1820198848.us-east-1.elb.amazonaws.com/
  - **_under construction_**
 
__Step 5.__ Migrate Data from Local MySQL to RDS using [MDS Strategy 1](https://aws.amazon.com/dms/) 
  - Create the RDS instance either through the AWS console or using CloudFormation.
  - Create the DMS replication instance and provision it in a subnet that can communicate with your non-RDS instance (source) and the RDS instance (target).
  - Create a Source Endpoint and a Target Endpoint. The DMS instance will use this connection information to connect to the databases.
  - Create the replication task.
  - The migration process will begin.
  - Verify data in the RDS instance.
  - Connecting the WebApplication to a DB Instance Running the MySQL RDS.
  - Verify WebApplication works normally, http://myalb-1820198848.us-east-1.elb.amazonaws.com/

__Step 6.__ Using Cloud Formation enable Raw Environment using `sceptre` 
  - docker pull cloudreach/sceptre:2.1.4
  - go to `cd cloud-formation`
  - you must configure you aws cli
  - docker run -v $(pwd):/project -v /home/me/.aws/:/root/.aws/:ro --name aws-sceptre cloudreach/sceptre::2.1.4
  - or if the docker is already done you will use `docker start -ia aws-sceptre`
  - `cd my-sceptre-raw-project/`
  - EC2 Stack, `sceptre create  dev/ec3-sample` please see Template into sceptre project [Here.](cloud-formation/my-sceptre-project/templates/ec2-sample.yaml)
  - RDS Mysql Stack, `sceptre create  dev/ec3-sample` please see Template into sceptre project [Here.](cloud-formation/my-sceptre-project/templates/rds-example-mysql.yaml)
  
## Refactoring / Re-architecting

![Monolithic Application to Microservices][img2]

### Activities

__Step 1,__ Move the application to Microservices using ECS.
  - **_under construction_**
  
__Step 2,__ Containerize the Monolith
  - **_under construction_**

__Step 3,__ Deploy the Monolith
- **_under construction_**

__Step 4.__ Break the Monolith
- **_under construction_**

__step 5.__ Deploy Microservices
- **_under construction_**

__Step 6.__ Using Cloud Formation enable **Optimized Environment**
  - `cd my-sceptre-raw-project/`
  - `sceptre create  dev/mb3-optimized.yaml`
  
  

[img0]: images/mb3-monolithic-app.png "Monolithic Application"
[img1]: images/mb3-monolithic_app-to-cloud.png "Monolithic Application to Cloud"
[img2]: images/mb3-microservices-app.png "Microservices Application"
