import sys
import socket
import json
import threading
import time
import os
import copy
current_node=sys.argv[1];
current_port=int(sys.argv[2]);
config=sys.argv[3];
d={};
dv={};
all_routers=[]
nexthop={}
displayLock=threading.Lock()
routing_table={}
pre_time={}
class Nodes:
     def __init__(self, current_node,current_port,config):
        self.current_node=current_node;
        self.current_port=current_port;
        direct_link={}
        neighbours=[]
        global config_file
        config_file={}
        self.direct_links=direct_link
        self.neighbours=neighbours
        fo = open(config, "r+");
        data=fo.read();
        nodes=(data.split());
        total_nodes=nodes[0];
        i=1;
        length=len(nodes);
        d[current_node]=[float(0),current_port]
        while (i!=length):
            d[nodes[i]]=[float(nodes[i+1]), int(nodes[i+2])]
            i+=3;
        value = d.items();
        i=0;
        length=len(d);
        while(i < length ):
            direct_link[value[i][0]]=value[i][1][0]
            if(value[i][0]!= current_node):
                neighbours.append(value[i][0])
            i+=1;
        dv[current_node]=direct_link
        config_file=dv.copy()
def Recv():
    recvIP="localhost"
    recvPort=current_port
    recv=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    recv.bind((recvIP,recvPort))
    dist_vctr={}
    dist_vector={}
    print ("SERVER HERE!\nThe server is ready to receive")
    while 1:
        current_time=time.time();
        message, clientAddress = recv.recvfrom(2048)
        dst_vector= json.loads(message)
        for key in dst_vector.keys():
            neighbor=key.encode('ascii','ignore')
        for key,val in dst_vector[neighbor].items():
            key=key.encode('ascii','ignore')
            dist_vector[key]=val
        dist_vctr[neighbor]=dist_vector.copy()
        dist_vector={}
        routing_table[current_node]=config_file[current_node].copy()
        routing_table.update(dist_vctr)
        for node in node1.neighbours:
            if neighbor not in pre_time.keys():
                pre_time[neighbor]=current_time;
            else:
                if node==neighbor and pre_time[neighbor] != float('INF'):
                    pre_time[neighbor]=current_time
                elif (node == neighbor and pre_time[neighbor] == float('INF')):
                    pre_time[neighbor]=current_time
                elif (node != neighbor and node in pre_time.keys()):
                    if current_time - pre_time[node] > 10:
                        pre_time[node] = float('INF')
                        del routing_table[current_node][node]
                        del routing_table[node]
                        del nexthop[node]
        for node in pre_time.keys():
             if (pre_time[node] == float('inf') and node in routing_table.keys() ):
                  del routing_table[current_node][node]
                  del routing_table[node]
        threading.Thread(target=bellman_ford, args=(routing_table,)).start()
    recv.close()
def Sender():
    while 1:
        port_list=[]
        for value in d.items():
            port_list.append(value[1][1]);
        serverIP="localhost"
        sender=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        strings = json.dumps(dv)
        for items in port_list:
            if int(items)!=current_port:
                sender.sendto(strings.encode(),(serverIP, int(items)))
        time.sleep(5)
        sender.close()
def bellman_ford(routing_table):
    my_neighbour=[]
    for node in routing_table:
        for neighbour in node1.neighbours:
            if(node == neighbour):
                my_neighbour.append(node)
    abc=[]
    for node in routing_table:
        for neighbour in routing_table[node]:
             if (neighbour in pre_time.keys()  and pre_time[neighbour]== float('inf')):
                pass
             else:
                abc.append(neighbour)
    my_set= set(abc)
    all_routers= list(my_set)
    for node in routing_table:
        for router in all_routers:
            if(router not in routing_table[node].keys()):
                     routing_table[node][router]=float('inf')
    for router in all_routers:
        for neighbour in my_neighbour:
            if (routing_table[current_node][router] > routing_table[neighbour][router] + routing_table[current_node][neighbour]):
                min_distance = routing_table[neighbour][router] + routing_table[current_node][neighbour]
                routing_table[current_node][router]=min_distance
                if(router in my_neighbour and config_file[current_node][router]<=min_distance):
                     routing_table[current_node][router]=config_file[current_node][router]
                     nexthop[router]= 'direct'
                else:
                     nexthop[router] = neighbour
            elif (len(nexthop.keys()) != len(all_routers)):
                nexthop[router] = 'direct'
            elif(router in my_neighbour and config_file[current_node][router] <= routing_table[current_node][router]):
                     routing_table[current_node][router]=config_file[current_node][router]
                     nexthop[router]= 'direct'
    dv[current_node] = routing_table[current_node]
    display()
def display():
        with displayLock:
            os.system("cls")
            print("\n I am Router " + current_node + '\n')
            for node in dv[current_node].keys():
                  print(" Least cost path to router " + node + " : through " + nexthop[node] + " with  cost " +  str("{0:.1f}".format(dv[current_node][node]) + "\n"))
node1=Nodes(current_node,current_port,config)
threading.Thread(target=Sender).start()
threading.Thread(target=Recv).start()