Mesos-marathon demo
=======

### Prepare the environnement

Just follow the instructions inside the `vagrant-mesos` directory. Once your vagrant machine is running with mesos and marathon installed you can continue with the following sections.

### Run the image

In order to deploy a new application in marathon it is just enough to make a Http POST

```
curl -XPOST -H "Content-Type:application/json" "http://192.168.33.10:8080/v2/apps" -d @/Users/johndoe/Documents/mesos-marathon/app.json
```

The contents of the json file obviously depends on the kind of applcation we want to deploy. The following 
sections contains several examples.


Install a tomcat server and deploy a war inside
-----
```
curl -i -H "Content-type: application/json" -X POST http://192.168.33.10:8080/v2/apps -d '
{
  "id": "tomcat",
  "cmd": "mv *.war apache-tomcat-*/webapps && cd apache-tomcat-* && sed \"s/8080/$PORT/g\" < ./conf/server.xml > ./conf/server-mesos.xml && ./bin/catalina.sh run -config ./conf/server-mesos.xml",
  "mem": 512,
  "cpus": 1.0,
  "instances": 1,
  "uris": [
    "http://wwwftp.ciril.fr/pub/apache/tomcat/tomcat-8/v8.0.20/bin/apache-tomcat-8.0.20.tar.gz",
    "https://gwt-examples.googlecode.com/files/Calendar.war"
  ]
}
'
```

Install a docker image and start it
-----
```
curl -i -H "Content-type: application/json" -X POST http://192.168.33.10:8080/v2/apps -d '
{
 "id": "exampleapp",
 "instances": 1,
 "cpus": 0.25,
 "mem": 128,
 "uris":[],
 "env": {  },
 "ports":[9000],
 "container": {
   "type": "DOCKER",
   "volumes": [],
   "docker": {
     "image": "fagossa/httpexample:latest",
     "network": "BRIDGE",
     "portMappings": [{ "containerPort": 8080, "servicePort": 9000 , "hostPort": 0, "protocol": "tcp" }]
    }
  }
}
'
```

It is also possible to create additional health checks to the installed applications by adding the following section to the json

```
"healthChecks": [
    {
      "protocol": "HTTP",
      "portIndex": 0,
      "path": "/",
      "gracePeriodSeconds": 5,
      "intervalSeconds": 20,
      "maxConsecutiveFailures": 3
    },
    {
      "protocol": "COMMAND",
      "command": { "value": "curl -f -X GET http://$HOST:$PORT" },
      "gracePeriodSeconds": 5,
      "intervalSeconds": 20,
      "maxConsecutiveFailures": 3
    }
]
 ``` 
