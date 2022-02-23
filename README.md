# A simple python app. Build & Run. 

## Build the image using the following command

```
$ docker build -t simple-flask-app:latest .
```

## Run the Docker container using the command shown below.

```
$ docker run --name=simple-flask-app-container -dp 5000:5000 simple-flask-app
```
