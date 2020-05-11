# Python Manual Install

A simple CRUD application using Flask and MySQL

Built With
 - Python 2.7
 - Python Libraries: flask and pymysql
 - MySQL


__NOTE:__ before starting, you will need to install Docker on your base system, following [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) 

1.- going to work directory `cd docker_approach/`


2.- we will create creating docker volume first, just to share data between container and local filesystem.
```
docker volume create --name mb3_data --opt type=none --opt device=~/path-to-project/master-builder-3/workspace --opt o=bind
```
3.- then, we will build Docker image:
```
docker build --no-cache -t "aws-mb/full-stack-mono-python:1.0" .
```

4.- create container using next command:
```
docker run -d --name mb-mono-python-v1 -p 5000:5000 --volume mb3_data:/workspace aws-mb/full-stack-mono-python:1.0
```
5.- next we will check tha container is running `docker ps`, will see output like this
```
CONTAINER ID        IMAGE                               COMMAND                  CREATED             STATUS              PORTS                              NAMES
e41e021bf1c1        aws-mb/full-stack-mono-python:2.0   "docker-entrypoint.s…"   6 minutes ago       Up 2 minutes        3306/tcp, 0.0.0.0:5000->5000/tcp   mb-mono-python-v1
```
6.- now, we will start our web Application using next command, `docker exec -d mb-mono-python-v1 python server.py`.

7.- validate the web application is alive on `http://localhost:5000/`
 


