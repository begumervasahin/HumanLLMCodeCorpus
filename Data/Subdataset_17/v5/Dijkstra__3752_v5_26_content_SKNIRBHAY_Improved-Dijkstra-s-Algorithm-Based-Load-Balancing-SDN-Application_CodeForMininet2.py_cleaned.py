from mininet.node import Host, OVSKernelSwitch
from mininet.topo import Topo
class FatTreeTopo(Topo):
    def __init__(self):
        super(FatTreeTopo, self).__init__()
        self.add_hosts()
        self.add_switches()
        self.create_host_links()
        self.create_switch_links()
    def add_hosts(self):
        hosts = {
            'h5': '10.0.0.5',
            'h6': '10.0.0.6',
            'h7': '10.0.0.7',
            'h8': '10.0.0.8'
        }
        for host_name, host_ip in hosts.items():
            self.addHost(host_name, cls=Host, ip=host_ip, defaultRoute=None)
    def add_switches(self):
        switches = ['s3', 's4', 's11', 's17', 's22']
        for switch_name in switches:
            self.addSwitch(switch_name, cls=OVSKernelSwitch)
    def create_host_links(self):
        host_links = [
            ('h5', 's3'),
            ('h6', 's3'),
            ('h7', 's4'),
            ('h8', 's4')
        ]
        for host, switch in host_links:
            self.addLink(host, switch)
    def create_switch_links(self):
        switch_links = [
            ('s3', 's11'),
            ('s11', 's4'),
            ('s4', 's22'),
            ('s3', 's22'),
            ('s11', 's17')
        ]
        for switch1, switch2 in switch_links:
            self.addLink(switch1, switch2)
topos = {'mytopo': (lambda: FatTreeTopo())}