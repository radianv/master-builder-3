# Master Builder 3

## AWS Services
With Amazon Web Services (AWS), you can provision compute power, storage and other resources, gaining access to a suite of elastic IT infrastructure services as your business demands them. With minimal cost and effort, you can move your application to the AWS cloud and reduce capital expenses, minimize support and administrative costs, and retain the performance, security, and reliability requirements your business demands.

## The Web Base application
A simple CRUD application using Flask and MySQL: 


![Monolithic Application][img0]

please see [Monolith Application](https://blog.heptio.com/what-is-a-monolithic-application-e375f5ad5ecb) 


This project has been based  on [this example](https://github.com/muhammadhanif/crud-application-using-flask-and-mysql), this Application is
docker based, the main objective of this project is elevate this Monolith to Miroservices, in order to achaive this 
we will install the Initial Web Application from example with just a bit modification,  we have two options:

   - Or using local based install (recommended), please see [Here](topics/my_local_monolith_install.md)
   
   - If you are familiar with docker you can use my docker approach, please see [Here](docker_approach/my_docker_monolith_install.md)
        
    
# Migrating your Existing Applications to the AWS Cloud

The strategy is using __"Forklift Migration Strategy"__, we will convert current approach from Monolithic to Microservices Application next steps below:

## Objectives of this solution
- Workload web appliction to cloud
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

Step 1, 

Step 2,

Step 3,  

## Refactoring / Re-architecting

![Monolithic Application to Microservices][img2]

### Activities

Step 1, 

Step 2,

Step 3,  



[img0]: images/mb3-monolithic-app.png "Monolithic Application"
[img1]: images/mb3-monolithic_app-to-cloud.png "Monolithic Application to Cloud"

