# crud-application-using-flask-and-mysql
A simple CRUD application using Flask and MySQL

### Built With

* Manual Installing Python:

Step 1:
```
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

Step 2:
```
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
```

Step 3:
```
sudo tar xzf Python-2.7.16.tgz
```

Step 4:
```
cd Python-2.7.16
sudo ./configure --enable-optimizations
sudo make altinstall

```

**Note**, Also if we don't have problems we will use `apt-get install python`

Step 5, installing `pip`, `pip install virtualenv`, `pip install virtualenvwrapper` and add in `.profile` next variables:
```
#virtualenvwrapper setup
export WORK_HOME=$HOME/envs
export PROJECT_HOME=$HOME/dev

source /usr/local/bin/virtualenvwrapper.sh

```

Creating docker volume,
```
docker volume create --name mb3_data --opt type=none --opt device=~/github/crud-monolith-application-using-flask-and-mysql/workspace --opt o=bind
```

Checking MySQL

```
docker logs mysql1 2>&1 | grep GENERATED
```

```
docker exec -it mysql1 mysql -uroot -p

```

Now we can start working on our Flask project:

1. Create a *virtualenvwrapper* using `mkproject HelloWorld`, if the project has been done, you can work on it using next command `workon HelloWorld`

2. Create `helloworld.py` the content looks like:

```
from flask import Flask


app = Flask(__name__)

@app.route('/index')
def index():
        return 'Hello world!'

if __name__== "__main__":
        app.run(host='0.0.0.0', port=5000) 
``` 

----------------------------------------------------------------------------------------------------------------


* Python Libraries: flask and pymysql
* MySQL
* AdminLTE 2

### Running on Docker

```
docker-compose up -d
```

After executing, you will have 2 running cointainers on your Docker host: `phonebook-app` and `phonebook-mysql`. For accessing the web application, open your browser and go to http://your-docker-host-ip-address:8181

To destroy the containers, execute:

```
docker-compose down --rmi all
```
