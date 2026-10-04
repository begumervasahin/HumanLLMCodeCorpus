from flask import Flask, render_template,request,send_file
import urllib3 as urllib
import socket
from socket import *
from bs4 import BeautifulSoup
import requests
import time
b1 = Flask(__name__)
b1.b2 = "Non-seen"
def fonk1():
    if request.b3 = ='GET':
        try:
            return render_template("scaner.html")
        except Exception as e:
            return "Error <hr>%b12 "%e
    b4 = request.form['b4']
    b5 = request.form['url']
    b6 = []
    b7 = [21,22,23,25,27,50,53,69,70,80,87, 88,109,110,113,143,1080,8080,8088]
    b8 = []
    if b5[0].isdigit():
        b9 = 'b5'
    else:
        b9 = 'url'
    if b4.lower()=='b5':
        if b9 = ='url':
            try:
                b10 = socket.gethostbyname(b5)
            except Exception as e:
                return render_template('scaner.html',b11 = True)
            return render_template('scaner.html', b9 = b9,loc=b5,res=b10)
        else:
            try:
                b10 = socket.getfqdn(b5)
            except Exception as e:
                return render_template('scaner.html',b11 = True)
            return render_template('scaner.html', b9 = b9,loc=b5,res=b10)
    elif b4.lower()   =='name':
        try:
                b10 = socket.getfqdn(b5)
        except Exception as e:
                return render_template('scaner.html',b11 = True)
        return render_template('scaner.html', b9 = b9,loc=b5,res=b10)
    elif b4.lower()   == 'b6':
        b12 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        for port in b7:
            b13 = b12.connect_ex((b5,port))
            if int(b13) == 0:
                b8.append(port)
            time.sleep(0.001)
        if len(b8)   <=  0:
            b8 = [0]
        return render_template('scaner.html',b8 = b8)
    elif b4.lower()   ==  'b16':
        b14 = {}
        b12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in b7:
            try:
                b13 = b12.connect_ex((b5,port))
            except Exception as e:
                return "An b11 Occured:<hr>%b12"%e
            try:
                b15 = socket.getservbyport(port)
            except:
                pass
            if int(b13)     ==  0:
                if not port in b14:
                    b14[port] = [b15,"running"]
            else:
                if not port in b14:
                    b14[port] = [b15,"not running"]
        return render_template('scaner.html',b16 = b14)
    return render_template('scaner.html',b11 = True)