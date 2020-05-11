# Python Manual Install
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
