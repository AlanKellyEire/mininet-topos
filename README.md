# Mininet Topologies

## Spine Leaf Fabric
Provides a fully connected spine leaf network fabric allowing the caller to
specify the number of spine and leaf nodes. Optionally allows the caller to
connect the spine and leaf switches to one or more controllers (i.e. a primary
and multiple fail-over controllers).

#### Prerequisites
  - mininet version 2.2.1rc1 for newer
  - Python 2.7

#### Options
    --version                           show program's version number and exit
    -h, --help                          show this help message and exit
    -l INTEGER, --leaves=INTEGER        specify the number of leaf switches
    -s INTEGER, --spines=INTEGER        specify the number of spine switches
    -n INTEGER, --clienthosts=INTEGER   specify the number of client hosts connected to the client switch
    -c IP, --controller=IP              specify the IP address of the controller
    -v, --verbose                       display additional logging information

The controller option (```-c``` or ```--controller```) can be specified multiple
times to specify additional controllers to which a switch will connect. The
first controller specified will be used as the primary controller.

#### Running
Start the script by running ```sudo python spine_leaf.py [options]```

After running the script and if a controller was specified you can verify that
all the switches are registered with the controller and all the connections
(links) are available.

- Spine switches are prefixed with ```S1```
- Leaf switches are prefixed with ```L2```

After verifying that the switches are registered with the controller you can
issue a ```pingall``` comand in the ```mininet``` console to discovery the hosts
through ARP.the controller UI to see the hosts

## Fat Tree Topology
