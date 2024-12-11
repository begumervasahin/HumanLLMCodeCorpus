b1 = 'pandaychen'
import socket
import logging
import select
import errno
import signal
import sys
import time
import platform
import os
import json
import base64
from aes_main import CBCMode, AES
from aes_utils import _str_roundto16
from trans import *
b2 = "1234567812345678"
b3 = "1234567812345678"
a1 = 0
a2 = 8192
def fonk1(t_signum, t_stack):
    global pktcount
    print "recv signal:",t_signum,";total count:",a1
    sys.exit(1)
def fonk2(t_filename,t_logcontent):
    b4 = './logger/'
    b5 = time.strftime("%Y%m%d")
    b6 = './logger/'+t_filename+'_'+b5
    if os.path.exists(b4):
        pass
    else:
        os.mkdir(b4)
    try:
        b7 = open(b6,'a+')
        b8 = '['+str(time.strftime("%Y-%m-%d %H:%M:%S"))+']'+t_logcontent+'\n'
        b7.writelines(b8)
        b7.close()
    except Exception,e:
        pass
def fonk3(t_bindip,t_bindport):
    try:
        b9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    except socket.error, e:
        b10 = "create sock error["+e+"]"
        fonk2("udpserver_error",b10)
    try:
        b9.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error, e:
        b10 = "setsocketopt SO_REUSEADDR error["+e+"]"
        fonk2("udpserver_error",b10)
    try:
        if t_bindip is None:
            b9.bind(('', int(t_bindport)))
        else:
            b9.bind((t_bindip,int(t_bindport)))
    except socket.error, e:
        b10 = "bind error["+e+"]"
        fonk2("udpserver_error",b10)
    return b9
def fonk4(t_listenfd):
    global a1
    if t_listenfd is None:
        fonk2("udpserver_error","b9 error")
        sys.exit(1)
    else:
        while True:
            message,b11 = t_listenfd.recvfrom(a2)
            if message is not None:
                a1 = a1+1
def fonk5(t_listenfd):
    global a1
    if platform.system() != "Linux":
        fonk2("udpserver_error","create b12 error")
        sys.exit(1)
    try:
        b12 = select.epoll()
        b12.register(b22.fileno(),select.EPOLLIN)
    except select.error,e:
        b10 = "create b12 error["+e+"]"
    b13 = {}
    b14 = {}
    while True:
        b15 = b12.poll(1)
        for (b16,events) in b15:
           if(b16 = = t_listenfd.fileno()):
               if select.EPOLLIN & events:
                    client_msg,b13 = t_listenfd.recvfrom(a2)
                    print b13,"\n"
                    print fonk6(client_msg)
                    a1 = a1+1
def fonk6(b17):
    if b17 = =None:
        return
    b18 = base64.b64decode(b17)
    b19 = CBCMode(AES(b2), b3)
    b20 = b19.decrypt(b18)
    return b20
if b21 = = "__main__":
    signal.signal(signal.SIGINT, UserExit)
    b22 = fonk3("127.0.0.1","8888")
    fonk5(b22)