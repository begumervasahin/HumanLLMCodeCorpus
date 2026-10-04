from mininet.node import CPULimitedHost, Host, OVSKernelSwitch
from mininet.topo import Topo
class class1(Topo):
    "Fat Tree Topology"
    def fonk1(self):
        "Create Fat tree Topology"
        super(class1, self).fonk1()
        b1 = self.addHost('b1', cls=Host, ip='10.0.0.5', defaultRoute=None)
        b2 = self.addHost('b2', cls=Host, ip='10.0.0.6', defaultRoute=None)
        b3 = self.addHost('b3', cls=Host, ip='10.0.0.7', defaultRoute=None)
        b4 = self.addHost('b4', cls=Host, ip='10.0.0.8', defaultRoute=None)
        b5 = self.addSwitch('b5', cls=OVSKernelSwitch)
        b6 = self.addSwitch('b6', cls=OVSKernelSwitch)
        b7 = self.addSwitch('b7', cls=OVSKernelSwitch)
        b8 = self.addSwitch('b8', cls=OVSKernelSwitch)
        b9 = self.addSwitch('b9', cls=OVSKernelSwitch)
        self.addLink(b1, b5)
        self.addLink(b2, b5)
        self.addLink(b3, b6)
        self.addLink(b4, b6)
        self.addLink(b5, b7)
        self.addLink(b7, b6)
        self.addLink(b6, b9)
        self.addLink(b5, b9)
        self.addLink(b7, b8)
b10 = {'mytopo': (lambda: class1())}