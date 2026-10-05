from pyretic.modules.routebellman import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
from pyretic.modules.wG_bellfordCost import *
class BellfordRoute(DynamicPolicy):
    def __init__(self):
        super(BellfordRoute, self).__init__()
        self.route_dict = {}
        self.topology = None
        self.network_dict = {}
        self.weighted_graph = None
        self.set_initial_state()
    def set_initial_state(self):
        self.query = packets(1, ['srcip'])
        self.query.register_callback(self.build_flow)
        self.forward = drop
        self.update_policy()
    def set_network(self, network):
        if self.topology and self.topology == network.topology:
            pass
        else:
            self.topology = network.topology
        self.weighted_graph = abileneCostList(self.topology)
        self.set_initial_state()
    def update_policy(self):
        self.policy = self.forward + self.query
    def build_flow(self, pkt):
        if pkt['dstip'] == IPAddr("10.0.0.1"):
            path_src_to_dst = build_path(self.topology, 1, pkt['switch'], pkt['inport'], self.weighted_graph)
            path1 = path_src_to_dst.bellford_routing()
            print(path1)
            dc = build_dic(IPAddr("10.0.0.1"), pkt['srcip'], path1)
            if IPAddr("10.0.0.1") in self.network_dict:
                self.network_dict[IPAddr("10.0.0.1")].update(dc[IPAddr("10.0.0.1")])
            else:
                self.network_dict.update(dc)
            path_dst_to_src = build_path(self.topology, pkt['switch'], 1, 1, self.weighted_graph)
            path2 = path_dst_to_src.bellford_routing()
            dc = build_dic(pkt['srcip'], IPAddr("10.0.0.1"), path2)
            if pkt['srcip'] in self.network_dict:
                self.network_dict[pkt['srcip']].update(dc[pkt['srcip']])
            else:
                self.network_dict.update(dc)
            self.forward = build_flowtable(self.network_dict)
        self.update_policy()
def main():
    return BellfordRoute()
