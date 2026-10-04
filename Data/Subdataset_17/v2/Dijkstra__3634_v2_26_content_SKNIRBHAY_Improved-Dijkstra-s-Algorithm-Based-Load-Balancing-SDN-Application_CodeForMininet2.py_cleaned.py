from mininet.node import CPULimitedHost, Host, OVSKernelSwitch
from mininet.topo import Topo
class FatTreeTopo(Topo):
    def __init__(self):
        super(FatTreeTopo, self).__init__()
        hosts = [
            ('h5', '10.0.0.5'),
            ('h6', '10.0.0.6'),
            ('h7', '10.0.0.7'),
            ('h8', '10.0.0.8')
        ]
        for host_name, host_ip in hosts:
            self.addHost(host_name, cls=Host, ip=host_ip, defaultRoute=None)
        switches = ['s3', 's4', 's11', 's17', 's22']
        for switch_name in switches:
            self.addSwitch(switch_name, cls=OVSKernelSwitch)
        self.addLink('h5', 's3')
        self.addLink('h6', 's3')
        self.addLink('h7', 's4')
        self.addLink('h8', 's4')
        self.addLink('s3', 's11')
        self.addLink('s11', 's4')
        self.addLink('s4', 's22')
        self.addLink('s3', 's22')
        self.addLink('s11', 's17')
topos = {'mytopo': (lambda: FatTreeTopo())}