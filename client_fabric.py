#!/usr/bin/python

'''
    Copyright (c) 2015 Ciena Corporation.
    All rights reserved. This program and the accompanying materials
    are made available under the terms of the Eclipse Public License v1.0
    which accompanies this distribution, and is available at
    http://www.eclipse.org/legal/epl-v10.html
'''

'''
client side mininet instance.
Topology: one client switch connected with multiple client hosts (specified by an argument)
clientfabric.py -n 4 -c 172.17.0.1 -c 172.17.0.2

'''

from optparse import OptionParser
import os
import sys
import time
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import OVSSwitch, Controller, RemoteController

######################################
######### Global Variables ###########
######################################
#clientSwitch=None


######################################
###### Define topologies here ########
######################################

#Data center Spine Leaf Network Topology
class clientTopo(Topo):
    "Linear topology of k switches, with one host per switch."

    def __init__(self, n, **opts):
        """Init.
            k: number of switches (and hosts)
            hconf: host configuration options
            lconf: link configuration options"""

        super(clientTopo, self).__init__(**opts)

        self.n = n


        clientSwitch = self.addSwitch('a%s%s' % (5,1)) #'a' for access switch ('c' for client was taken by 'c' for controller)

        for i in irange(0, n-1):
            host= self.addHost('h%s%s' % (5, (i+1)))
            self.addLink(clientSwitch, host)
            


def simpleTest(options):
    # argument to put in either remote or local controller
    controllers = None
    if options.controllers:
        controllers = []
        "Create remote controller to which switches are attached"
        for idx, addr in enumerate(options.controllers):
            controllers.append(RemoteController( "c%d" % idx, ip=addr))

    class MultiSwitch( OVSSwitch ):
        "Custom Switch() subclass that connects to different controllers"
    def start( self, controllers ):
        return OVSSwitch.start( self, [ cmap[ self.name ] ] )

    topo = clientTopo(n=options.client_host_count)    
    net = Mininet(  topo=topo, switch=MultiSwitch, build=False)

    cmap = { 'clientSwitch': controllers[0:]}
    for c in controllers or []:
        net.addController(c)

    net.build()

    for c in controllers or []:
        c.start()

    #clientSwitch.start([controllers[0:]])
    
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)


    CLI( net )
    net.stop()

if __name__ == '__main__':
    parser = OptionParser(version="%prog 1.0")

    parser.add_option("-n", "--clienthosts", dest="client_host_count",
        help="specify the number of client side hosts connected to the client switch",
    	metavar="INTEGER", type="int", default=3)
    parser.add_option("-c", "--controller", dest="controllers",
        help="specify the IP address of the controller",
        action="append", metavar="IP")
    parser.add_option("-v", "--verbose", dest="verbose",
        help="display additional logging information",
        action="store_true", default=False)

    (options, args) = parser.parse_args()

    if options.verbose:
        setLogLevel('debug')
    else:
        setLogLevel('info')
    simpleTest(options)