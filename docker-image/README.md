Docker image
=======
This is the base docker image to be installed inside **mesos**. It's composed of a basic python server that serves an index.html. In order to run it you must have docker installed. So, you could be in one of this scenarios:

Windows and Mac
-----
TODO: install boot2docker


Once your docker environment is up and running, you could proceed to building and running your image.


Handling the image
-----
 
### Create a Docker image
`docker build -t fagossa/httpexample .`
This will create the docker image based on the **Dockerfile** provided. You could verify the list of available images by executing the following command `docker images`


### Run the image
`docker run -p 9090:8080 fagossa/httpexample`

if we execute a `docker ps` we should be able to see our newly created image in the list!

`CONTAINER ID   IMAGE                       COMMAND              PORTS `    
`50226338cfe2   fagossa/httpexample:latest "/env/bin/python -m   0.0.0.0:49176->8080/tcp`

However, in order access it, you need to first verify the address in which docker is running. If you are using boot2docker, you could just get it by running `boot2docker ip`.

Assuming that your boot2docker is running in **192.168.59.103**, you could access the service by pointing to `http://192.168.59.103:9090`
