# vagrant-mesos [![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/everpeace/vagrant-mesos?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Spin up your [Mesos](http://mesos.apache.org) Cluster with [Vagrant](http://www.vagrantup.com)! (Both Virtualbox and AWS are supported.)

This spins up Mesos 0.21.0 cluster and also spins up a framework server node in which [Marathon](https://github.com/mesosphere/marathon) (0.8.0) and [Chronos](http://github.com/mesos/chronos) (2.1.0) are runinng.  This means you can build your own __Mesos+Marathon+Chronos+Docker__ PaaS with `vagrant up`!!  Marathon works as distributed `init.d` and Chronos works as distributed `cron`!!  _If you wanted to deploy docker containers, please refer to the chapter "Deploy Docker Container with Marathon" in [thig blog entry](http://frankhinek.com/deploy-docker-containers-on-mesos-0-20/)._

* Using VirtualBox
	* [Mesos Standalone on VirtualBox](#svb)
	* [Mesos Cluster on VirtualBox](#clvb)
* Using Amazon EC2
	* [Mesos Standalone on EC2](#sec2)
	* [Mesos Cluster on EC2 (VPC)](#clec2)

The mesos installation is powered by mesos chef cookbook.  Please see [everpeace/cookbook-mesos](http://github.com/everpeace/cookbook-mesos).

Base boxes used in `Vagrantfile`s are Mesos pre-installed boxes, [everpeace/mesos](https://vagrantcloud.com/everpeace/boxes/mesos) shared on Vagrant Cloud.

Prerequisites
----
* vagrant 1.6.5+: <http://www.vagrantup.com/>
* VirtualBox: <https://www.virtualbox.org/> (not required if you use ec2.)
* vagrant plugins
    * [vagrant-omnibus](https://github.com/schisamo/vagrant-omnibus)
          `$ vagrant plugin install vagrant-omnibus`
    * [vagrant-berkshelf](https://github.com/berkshelf/vagrant-berkshelf) (>=4.0.0)
          `$ vagrant plugin install vagrant-berkshelf`
		* To use vagrant-berkself, you will have to install [ChefDK](http://getchef.com/downloads/chef-dk).
    * [vagrant-hosts](https://github.com/adrienthebo/vagrant-hosts)
          `$ vagrant plugin install vagrant-hosts`
    * [vagrant-cachier](https://github.com/fgrehm/vagrant-cachier)
          `$ vagrant plugin install vagrant-cachier`
    * [vagrant-aws](https://github.com/mitchellh/vagrant-aws) (only if you use ec2.)
    	   `$ vagrant plugin install vagrant-aws`

<a name="svb"></a>
Mesos Standalone on VirtualBox
----
It's so simple!

    $ cd standalone
    $ vagrant up

After box is up, you can see services running at:

* Mesos web UI on: <http://192.168.33.10:5050>
* [Marathon](https://github.com/mesosphere/marathon) web UI on: <http://192.168.33.10:8080>
* [Chronos](https://github.com/mesos/chronos) web UI on: <http://192.168.33.10:8081>

<a name="sec2"></a>
Mesos Standalone on EC2
----
1. set ec2 credentials and some configurations defined in `standalone/aws_config.yml`. You have to fill up `EDIT_HERE` parts.  Security group you'll set must accept at least tcp port 22(SSH) and 5050(mesos-master web ui) from outside of ec2.

		# Please set AWS credentials
		access_key_id:  EDIT_HERE
		secret_access_key: EDIT_HERE

		# please choose one from
		# ["ap-northeast-1", "ap-southeast-1", "eu-west-1", "sa-east-1", "us-east-1",
		#  "us-west-1", "ap-southeast-2", "us-west-2"]
		region: us-east-1

		# array of security groups. e.g. ['sg*** ']
		security_groups: EDIT_HERE

		# see http://aws.amazon.com/ec2/instance-types/#selecting-instance-types
		# for other instance types and its specs.
		instance_type: m1.small

		keypair_name: EDIT_HERE

		ssh_private_key_path: EDIT_HERE

2. you can spin up mesos box on ec2 by the same way with the case of virtual box

        cd standalone
        vagrant up --provider=aws

   After box is up, you can see services running at:

   * Mesos web UI on: `http://#_public_dns_of_the_VM_#:5050`
   * [Marathon](https://github.com/mesosphere/marathon) web UI on: `http://#_public_dns_of_the_VM_#:8080`
   * [Chronos](https://github.com/mesos/chronos) web UI on: `http://#_public_dns_of_the_VM_#:8081`


	_Tips: you can get public dns of the vm by:_

	```
	$ vagrant ssh -- 'echo http://`curl --silent http://169.254.169.254/latest/meta-data/public-hostname`:5050'
	http://ec2-54-193-24-154.us-west-1.compute.amazonaws.com:5050
	```
