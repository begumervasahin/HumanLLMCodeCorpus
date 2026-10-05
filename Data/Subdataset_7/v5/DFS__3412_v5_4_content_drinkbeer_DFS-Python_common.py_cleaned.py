import socket
import sys
import json
import os
import logging
logging.basicConfig(b1 = sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
b2 = logging.getLogger()
b2.setLevel(logging.CRITICAL)
a1 = -1
a2 = -1
a3 = -1
b3 = ''
a4 = 50008
a5 = 50009
a6 = 50010
b4 = {"s1": a5, "s2": a6}
b5 = "s1"
b6 = "s2"
b7 = {
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
def fonk1(command, param_list):
    b8 = {'command': command, 'param_list': param_list}
    return json.dumps(b8)
def fonk2(result):
    return json.dumps(result)