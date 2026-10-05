import socket
import sys
import json
import os
import logging
logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()
log.setLevel(logging.CRITICAL)
client_sock = -1
server1_sock = -1
server2_sock = -1
HOST = ''
MASTER_PORT = 50008
SERVER1_PORT = 50009
SERVER2_PORT = 50010
SERVER_PORTS = {"s1": SERVER1_PORT, "s2": SERVER2_PORT}
DIR_S1 = "s1"
DIR_S2 = "s2"
DFS_COMMANDS = {
    'ACCESS': 1,
    'CHMOD': 2,
    'CHOWN': 3,
    'GETATTR': 4,
    'READDIR': 5,
    'READLINK': 6,
    'MKNOD': 7,
    'RMDIR': 8,
    'MKDIR': 9,
    'STATFS': 10,
    'UNLINK': 11,
    'SYMLINK': 12,
    'RENAME': 13,
    'LINK': 14,
    'UTIMENS': 15,
    'OPEN': 16,
    'CREATE': 17,
    'READ': 18,
    'WRITE': 19,
    'TRUNCATE': 20,
    'FLUSH': 21,
    'RELEASE': 22,
    'FSYNC': 23
}
def stringify_command(command, param_list):
    command_obj = {'command': command, 'param_list': param_list}
    return json.dumps(command_obj)
def stringify_result(result):
    return json.dumps(result)