import sys
import socket
import select
import json
import threading
import time
import copy
import signal
RECV_BUFFER = 4096
INFINITY = float('inf')
self_address = ""
neighbors = {}
routing_table = {}
adjacent_links = {}
old_links = {}
active_history = {}
dead_links = []
recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
def main():
    global self_address
    if len(sys.argv) < 3:
        print("usage: bfclient.py <localport> <timeout> <[id_addr1 port1 weight1...]>")
        sys.exit()
    local_port = int(sys.argv[1])
    recv_socket.bind(('', local_port))
    signal.signal(signal.SIGINT, close_handler)
    host = socket.gethostbyname(socket.gethostname())
    self_address = f"{str(host)}:{sys.argv[1]}"
    timeout_interval = int(sys.argv[2])
    parse_neighbors(sys.argv[3:])
    print(f"bfclient running at address [{str(host)}] on port [{sys.argv[1]}]")
    update_timer(timeout_interval)
    node_timer(timeout_interval)
    prompt()
    while True:
        handle_inputs()
    recv_socket.close()
def prompt():
    sys.stdout.write('> ')
    sys.stdout.flush()
def update_neighbor():
    for neighbor in copy.deepcopy(neighbors):
        addr = parse_address(neighbor)
        send_dict = {'type': 'update', 'routing_table': {}}
        routing_table_copy = copy.deepcopy(routing_table)
        for node in routing_table_copy:
            send_dict['routing_table'][node] = routing_table_copy[node]
            if node != neighbor and routing_table_copy[node]['link'] == neighbor:
                send_dict['routing_table'][node]['cost'] = INFINITY
        recv_socket.sendto(json.dumps(send_dict), addr)
def update_timer(timeout_interval):
    update_neighbor()
    t = threading.Timer(timeout_interval, update_timer, [timeout_interval])
    t.setDaemon(True)
    t.start()
def node_timer(timeout_interval):
    for neighbor in copy.deepcopy(neighbors):
        if neighbor in active_history:
            time_threshold = (3 * timeout_interval)
            if (int(time.time()) - active_history[neighbor]) > time_threshold:
                if routing_table[neighbor]['cost'] != INFINITY:
                    close_inactive_connection(neighbor)
        start_time = int(time.time())
        t = threading.Timer(3, node_timer, [timeout_interval])
        t.setDaemon(True)
        t.start()
def parse_neighbors(args):
    if len(args) % 3 != 0:
        print("invalid link inputs (each link requires 3 parameters).")
        sys.exit()
    for i in range(0, len(args), 3):
        neighbor_address = f"{socket.gethostbyname(args[i])}:{args[i + 1]}"
        routing_table[neighbor_address] = {'cost': float(args[i + 2]), 'link': neighbor_address}
        adjacent_links[neighbor_address] = float(args[i + 2])
        neighbors[neighbor_address] = {}
def handle_inputs():
    socket_list = [sys.stdin, recv_socket]
    try:
        read_sockets, _, _ = select.select(socket_list, [], [])
    except (select.error, socket.error) as e:
        sys.exit()
    for sock in read_sockets:
        if sock == recv_socket:
            handle_received_data()
        else:
            handle_user_input()
def handle_received_data():
    data, addr = recv_socket.recvfrom(RECV_BUFFER)
    if data:
        msg = json.loads(data)
        msg_handler(msg, addr)
    else:
        print("[Error] 0 bytes received.")
def handle_user_input():
    data = sys.stdin.readline().rstrip()
    if len(data) > 0:
        data_list = data.split()
        cmd_handler(data_list)
        prompt()
    else:
        sys.stdout.flush()
        prompt()
def cmd_handler(args):
    if args[0] == "LINKDOWN":
        if len(args) == 3:
            link_down(args[1], args[2])
        else:
            print("[ERROR] incorrect number of args for 'LINKDOWN' command.")
    elif args[0] == "LINKUP":
        if len(args) == 3:
            link_up(args[1], args[2])
        else:
            print("[ERROR] incorrect number of args for 'LINKUP' command.")
    elif args[0] == "SHOWRT":
        show_routing_table()
    elif args[0] == "TWEET":
        tweet_content = ' '.join(args[1:])
        tweet(self_address, tweet_content)
    elif args[0] == "CLOSE":
        close()
def msg_handler(received_data, tuple_addr):
    global self_address
    table_changed = False
    t_now = int(time.time())
    addr = parse_address(tuple_addr)
    if received_data['type'] == 'update':
        handle_update_message(received_data, addr, t_now, table_changed)
def close_handler(signum, frame):
    sys.exit(f"signal {str(signum)} called, closing down.")
def link_down(ip_addr, port):
    node_address = f"{ip_addr}:{port}"
    if node_address not in neighbors:
        print(f"[ERROR] {node_address} is not a neighbor.")
    else:
        cost = adjacent_links[node_address]
        old_links[node_address] = cost
        if routing_table[node_address]['cost'] != INFINITY:
            routing_table[node_address]['cost'] = INFINITY
            routing_table[node_address]['link'] = "n/a"
        update_routing_table_after_link_change(node_address)
        pair_key = f"{self_address},{node_address}"
        dead_links.append(pair_key)
        send_link_down_message(pair_key)
        del neighbors[node_address]
def link_up(ip_addr, port):
    node_address = f"{ip_addr}:{port}"
    if node_address not in old_links:
        print("[Error] This link does not exist.")
    else:
        routing_table[node_address]['cost'] = old_links[node_address]
        del old_links[node_address]
        routing_table[node_address]['link'] = node_address
        neighbors[node_address] = {}
        handle_link_up_reactivation(node_address)
def tweet(sender_id, message):
    timestamp = time.strftime('%H:%M:%S', time.localtime(time.time()))
    tweet_msg = f"[{timestamp}] @{sender_id}: {message}"
    send_tweet_message(tweet_msg)
def show_routing_table():
    timestamp = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print(f"[{timestamp}] Distance vector list for [{self_address}] is:")
    for node in routing_table:
        link = routing_table[node]['link']
        print(f"Destination = ({node}), Cost = {routing_table[node]['cost']}, Link = ({link})")
def parse_address(addr):
    return f"{addr[0]}:{addr[1]}"
if __name__ == "__main__":
    main()