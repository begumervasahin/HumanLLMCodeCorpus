from mininet.node import CPULimitedHost, Host, OVSKernelSwitch
from mininet.topo import Topo
class class1(Topo):
    def fonk1(self):
        super(class1, self).fonk1()
        b1 = [
            ('h5', '10.0.0.5'),
            ('h6', '10.0.0.6'),
            ('h7', '10.0.0.7'),
            ('h8', '10.0.0.8')
        ]
        for host_name, host_ip in b1:
            self.addHost(host_name, b2 = Host, ip=host_ip, defaultRoute=None)
        b3 = ['s3', 's4', 's11', 's17', 's22']
        for switch_name in b3:
            self.addSwitch(switch_name, b2 = OVSKernelSwitch)
        self.addLink('h5', 's3')
        self.addLink('h6', 's3')
        self.addLink('h7', 's4')
        self.addLink('h8', 's4')
        self.addLink('s3', 's11')
        self.addLink('s11', 's4')
        self.addLink('s4', 's22')
        self.addLink('s3', 's22')
        self.addLink('s11', 's17')
b4 = {'mytopo': (lambda: class1())}