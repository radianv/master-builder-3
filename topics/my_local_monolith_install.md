# Project setup steps on local

A simple CRUD application using Flask and MySQL

Built With
 - Python 2.7
 - Python Libraries: flask and pymysql
 - MySQL
 
1.- Install python & pip, there two ways, first doing manual install please see [Here](python_manual_install.md) (this is optional, just another old school way...) in this case we will use 
next steps  `sudo apt-get install python` then install pip `sudo apt-get install python-pip`.

2.- Installing additional libraries `pip install virtualenv`, `pip install virtualenvwrapper`. 

3.- Next add in `vi ~/.profile` or `vi ~/.bashrc` next variables:
```
#virtualenvwrapper setup

export WORK_HOME=$HOME/envs
export PROJECT_HOME=$HOME/dev

source /usr/local/bin/virtualenvwrapper.sh

```

then reload new variables using `. ~/.profile` or `source ~/.bashrc` depends on what's in there, more info please see [the functional differences between `.profile` `.bash_profile` and `.bashrc`](https://serverfault.com/questions/261802/what-are-the-functional-differences-between-profile-bash-profile-and-bashrc) 


4.- Install MySQL, [A Quick Guide to Using the MySQL APT Repository](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-fresh-install)

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
 - ypu will see `Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)` 