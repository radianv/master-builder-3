# Migrating your Existing Applications to the AWS Cloud

## AWS Services
With Amazon Web Services (AWS), you can provision compute power, storage and other resources, gaining access to a suite of elastic IT infrastructure services as your business demands them. With minimal cost and effort, you can move your application to the AWS cloud and reduce capital expenses, minimize support and administrative costs, and retain the performance, security, and reliability requirements your business demands.

## The Web Base application
A simple CRUD application using Flask and MySQL: 


![Monolithic Application][img0]

please see [Monolith Application](https://blog.heptio.com/what-is-a-monolithic-application-e375f5ad5ecb) 


This project has been based  on `https://github.com/muhammadhanif/crud-application-using-flask-and-mysql`, this Application is
docker based, the main objective of this project is use [Monolith Application](https://blog.heptio.com/what-is-a-monolithic-application-e375f5ad5ecb), for this project propose it we have two ways:

   - My docker approach, please see [Here](docker_approach/my_docker_monolith_install.md])
   
   - Or using local based install, please see [Here](topics/my_local_monolith_install.md)  
    

Following the strategy __Migrating your Existing Applications to the AWS Cloud__ using __"Forklift Migration Strategy"__, we will convert current approach from Monolithic to Microservices Application next steps below:

   1. Rehosting & Replatforming , lift-tinker-and-shift.
   2. Refactoring / Re-architecting

## Rehosting & Replatforming , lift-tinker-and-shift.

## Refactoring / Re-architecting



[img0]: images/mb3-monolithic-app.png "Monolithic Application"