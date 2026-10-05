
import inspect
import os
import sys
from mininext.topo import Topo
from mininext.services.quagga import QuaggaService
from collections import namedtuple
b1 = namedtuple("b1", "name ip")
b2 = None
class class1(Topo):
	"Creates a topology of ChordDFS routers"
	def fonk1(self, num_nodes):
		Topo.fonk1(self)
		b3 = []
		for node in range(num_nodes):
			b4 = self.addHost(name='n{0}'.format(node+1), ip='172.1.1.{0}/24'.format(node+1))
			b3.append(b4)
			if not os.path.exists("nodes/n{0}".format(node+1)):
				os.makedirs("nodes/n{0}".format(node+1))
				os.makedirs("nodes/n{0}/files".format(node+1))
				os.makedirs("nodes/n{0}/files/chord".format(node+1))
				os.makedirs("nodes/n{0}/files/client".format(node+1))
				os.makedirs("nodes/n{0}/logs".format(node+1))
			else:
				for root, dirs, files in os.walk("nodes", b5 = False):
					b6 = root.split("/")
					if b6[-1] != "client":
						for f in files:
							os.remove(os.path.join(root,f))
		b7 = self.addSwitch('sw1')
		for node in b3:
			self.addLink(node, b7)