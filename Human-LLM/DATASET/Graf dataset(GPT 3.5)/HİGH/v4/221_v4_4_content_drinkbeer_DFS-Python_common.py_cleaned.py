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
a7 = 1
a8 = 2
a9 = 3
a10 = 4
a11 = 5
a12 = 6
a13 = 7
a14 = 8
a15 = 9
a16 = 10
a17 = 11
a18 = 12
a19 = 13
a20 = 14
a21 = 15
a22 = 16
a23 = 17
a24 = 18
a25 = 19
a26 = 20
a27 = 21
a28 = 22
a29 = 23
def fonk1(command, param_list):
    b7 = {'command': command, 'param_list': param_list}
    return json.dumps(b7)
def fonk2(result):
    return json.dumps(result)