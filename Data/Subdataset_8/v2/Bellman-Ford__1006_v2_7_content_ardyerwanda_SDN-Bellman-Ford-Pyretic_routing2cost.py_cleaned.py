from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
class BellfordRoute(DynamicPolicy):
    def __init__(self):
        super(BellfordRoute, self).__init__()
        self.route_dict = {}
        self.topology = None
        self.dictionary = {}
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
    def build_flow(self, packet):
        if packet['dstip'] == IPAddr("10.0.0.1"):
            path_src_to_dst = build_path(self.topology, 1, packet['switch'], packet['inport'], self.weighted_graph)
            path1 = path_src_to_dst.bellford_routing()
            print(path1)
            dict1 = build_dic(IPAddr("10.0.0.1"), packet['srcip'], path1)
            if IPAddr("10.0.0.1") in self.dictionary:
                self.dictionary[IPAddr("10.0.0.1")].update(dict1[IPAddr("10.0.0.1")])
            else:
                self.dictionary.update(dict1)
            path_dst_to_src = build_path(self.topology, packet['switch'], 1, 1, self.weighted_graph)
            path2 = path_dst_to_src.bellford_routing()
            dict2 = build_dic(packet['srcip'], IPAddr("10.0.0.1"), path2)
            if packet['srcip'] in self.dictionary:
                self.dictionary[packet['srcip']].update(dict2[packet['srcip']])
            else:
                self.dictionary.update(dict2)
            self.forward = build_flowtable(self.dictionary)
        self.update_policy()
def main():
    return BellfordRoute()
