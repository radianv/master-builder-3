# Python Manual Install
before starting, you will need to install Docker on your base system, following (Install Docker Engine on Ubuntu)[https://docs.docker.com/engine/install/ubuntu/] 



Creating docker volume,
```
docker volume create --name mb3_data --opt type=none --opt device=~/github/crud-monolith-application-using-flask-and-mysql/workspace --opt o=bind
```
