# Containers Demo

### Containers Demo

1) Change into the `DockerDemo` directory

```
$ cd DockerDemo
```

2) Edit the `app.py` file to add your name. Keep the secret message the same.

3) Build the container with your source code changes, tag it with the name `myapiserver`

```
$ docker build -t myapiserver .
```

4) Check to make sure the image you just built exists on your machine

```
$ docker images
```

5) Run an instance of the container

```
$ docker run --name importantapi -d -p 5001:5000 myapiserver
```

6) Use curl or postman to figure out the passphrase (API is accessible on your host machine over `localhost:5001`)

7) View the logs from outside the container

```
$ docker logs importantapi
```

8) Stop the container

``` 
$ docker stop myapiserver
```

0) Remove the container from your machine

```
$ docker rm myapiserver
```