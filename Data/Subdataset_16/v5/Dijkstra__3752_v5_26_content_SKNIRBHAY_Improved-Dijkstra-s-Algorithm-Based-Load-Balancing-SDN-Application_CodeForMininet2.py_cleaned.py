from mininet.node import Host, OVSKernelSwitch
from mininet.topo import Topo
class class1(Topo):
    def fonk1(self):
        super(class1, self).fonk1()
        self.fonk2()
        self.fonk3()
        self.fonk4()
        self.fonk5()
    def fonk2(self):
        b1 = {
            'h5': '10.0.0.5',
            'h6': '10.0.0.6',
            'h7': '10.0.0.7',
            'h8': '10.0.0.8'
        }
        for host_name, host_ip in b1.items():
            self.addHost(host_name, b2 = Host, ip=host_ip, defaultRoute=None)
    def fonk3(self):
        b3 = ['s3', 's4', 's11', 's17', 's22']
        for switch_name in b3:
            self.addSwitch(switch_name, b2 = OVSKernelSwitch)
    def fonk4(self):
        b4 = [
            ('h5', 's3'),
            ('h6', 's3'),
            ('h7', 's4'),
            ('h8', 's4')
        ]
        for host, switch in b4:
            self.addLink(host, switch)
    def fonk5(self):
        b5 = [
            ('s3', 's11'),
            ('s11', 's4'),
            ('s4', 's22'),
            ('s3', 's22'),
            ('s11', 's17')
        ]
        for switch1, switch2 in b5:
            self.addLink(switch1, switch2)
b6 = {'mytopo': (lambda: class1())}