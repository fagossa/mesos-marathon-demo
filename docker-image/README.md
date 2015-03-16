Docker image
=======
This is the base docker image to be installed inside **mesos**. It's composed of a basic python server that serves an index.html. In order to run it you must have docker installed. So, you could be in one of this scenarios:

Windows and Mac
-----
Follow this instructions if you are using [Mac](https://docs.docker.com/installation/mac/) or [Windows](https://docs.docker.com/installation/windows/). Once everything is installed, be sure to start the process for example by running `boot2docker up`.


Once your docker environment is up and running, you could proceed to building and running your image.


Handling the image
-----
 
### Create a Docker image
In order to create a docker image based on the *Dockerfile* provided execute this command

`docker build -t imgname/httpexample .`

 You could verify the list of available images by executing the following command `docker images`


### Run the image
To instantiate our application we should execute the following command
`docker run -p 9090:8080 imgname/httpexample`

Where,
 * p, means the port mapping
 * imgname/httpexample, means the image name

Then, if we execute a `docker ps` we should be able to see our newly created image on the list!

`CONTAINER ID   IMAGE                       COMMAND              PORTS `    
`50226338cfe2   imgname/httpexample:latest "/env/bin/python -m   0.0.0.0:49176->9090:8080/tcp`

However, in order access it, you need to first verify the address in which docker is running. If you are using *boot2docker*, you could just get it by running `boot2docker ip`.

Assuming that your boot2docker is running in **192.168.59.103**, you could access the service by pointing to `http://192.168.59.103:9090`
