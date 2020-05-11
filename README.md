# Migrating your Existing Applications to the AWS Cloud

## AWS Services
With Amazon Web Services (AWS), you can provision compute power, storage and other resources, gaining access to a suite of elastic IT infrastructure services as your business demands them. With minimal cost and effort, you can move your application to the AWS cloud and reduce capital expenses, minimize support and administrative costs, and retain the performance, security, and reliability requirements your business demands.

## The Web Base application
A simple CRUD application using Flask and MySQL, this project has been based  on `https://github.com/muhammadhanif/crud-application-using-flask-and-mysql`, this Application is
docker based (my docker approach, please see (here)[topics/my_docker_monolith_install.md]), the main objective of this project is use [Monolith Application](https://blog.heptio.com/what-is-a-monolithic-application-e375f5ad5ecb), regarding that, we will convert current approach to monolithic next steps below:

### Project setup steps

1.- Install python & pip, there two ways to do that manual install [here](topics/python_manual_install.md) (this is optional, just another old school way...) in this case we will use 
next steps  `sudo apt-get install python` then install pip `sudo apt-get install python-pip`.

2.- Installing additional libraries `pip install virtualenv`, `pip install virtualenvwrapper`. 

3.- Next add in `vi ~/.profile` or `vi ~/.bashrc` next variables:
```
#virtualenvwrapper setup

export WORK_HOME=$HOME/envs
export PROJECT_HOME=$HOME/dev

source /usr/local/bin/virtualenvwrapper.sh

```

then reload new variables using `. ~/.profile` or `source ~/.bashrc` (depends on what in there, more info plese see (the functional differences between `.profile` `.bash_profile` and `.bashrc`)[https://serverfault.com/questions/261802/what-are-the-functional-differences-between-profile-bash-profile-and-bashrc]) 


4.- Install MySQL, (A Quick Guide to Using the MySQL APT Repository)[https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-fresh-install]

5.- Creating MySQL Database and webapp Schemas, you must connect to MySQL using root `mysql -u root -p`:
```
CREATE DATABASE crud_mono_flask;
```
Creating MySQL Data base user:
```
CREATE USER 'dev'@'%' IDENTIFIED BY 'dev_password';
```
Grand all privileges to a user account over a specific database:
```
GRANT ALL PRIVILEGES ON crud_mono_flask.* TO 'dev'@'%';
```
6.- Installing Monolith WebApplication

 - Clone this repository `git clone https://github.com/radianv/master-builder-3.git`
 - Then `cd master-builder-3/workspace/dev/mb3/`
 - Enable virtualenv project `mkvirtualenv mb3` and install dependencies `pip install Flask` and `pip install pymysql`
 - next execute `python server.py`
 - ypu will see `Running on http://0.0.0.0:80/ (Press CTRL+C to quit)` 
 
