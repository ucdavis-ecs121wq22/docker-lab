# Docker CheatSheet

## To Build a Docker image using the following command inside the app's root directory

```
$ docker build -t IMAGE_NAME:IMAGE_TAG PATH_OF_THE_DOCKERFILE
```

## Run the Docker container using the command shown below.

```
$ docker run IMAGE_NAME:IMAGE_TAG
```

There are options available to add more functionalities to running a docker container, like port-mapping, binding volume mounts, detaching from the current console etc. 
You can view those options by running: 

```
$ docker run --help
```

## To view the container files 

You need the container name or the container ID to go into an interactive shell of the docker container. You can do using:

```
$ docker container list
```

Then, you can execute the following command to view the container:

```
$ docker exec -it CONTAINER_ID/CONTAINER_NAME bash
```

The application will be accessible at `http://127.0.0.1:5000` or if you are using boot2docker then first find IP address using ```$ boot2docker ip``` and the use the IP `http://HOST_IP:5000`

## To prune any unused containers 

To remove any of the containers that are not being used anymore, you can use the following command: 

```
$ docker container prune
```

## To prune unused images

To remove ununsed images, you can use the following command:

```
$ docker images prune
```

## To view details of a container

For viewing details of a specific container, docker has an `inspect` command available: 

```
$ docker container inspect CONTAINER_ID/CONTAINER_NAME
```

## To pull an image from the DockerHub: 

There are thousands of docker images available on DockerHub, to pull any public image available: 

```
$ docker pull IMAGE_NAME:IMAGE_TAG
```

## To view complete list of commands supported by Docker in the Dockerfile

There are a lot of commands that are supported in the Dockerfile. Here is the [link](https://docs.docker.com/engine/reference/builder/) to their official documentation.