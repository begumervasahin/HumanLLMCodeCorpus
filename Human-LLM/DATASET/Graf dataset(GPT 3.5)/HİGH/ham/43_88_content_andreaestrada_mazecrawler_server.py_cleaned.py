import socket
import threading
from queue import Queue
import fileinput
import main
import spec
import sys
b1 = ""
a1 = 0
def fonk1():
  import spec
  b1 = spec.host
  a1 = int(spec.port)
  a2 = 2
  b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  b2.bind((b1,a1))
  b2.listen(a2)
  print("Waiting for players...")
  def fonk2(client, b12, cID, b11):
    client.setblocking(1)
    b3 = ""
    while True:
      try:
        b3 += client.recv(10).decode("UTF-8")
        b4 = b3.split("\n")
        while (len(b4) > 1):
          b5 = b4[0]
          b3 = "\n".join(b4[1:])
          b12.put(str(cID) + " " + b5)
          b4 = b3.split("\n")
      except: return
  def fonk3(b11, b12):
    while True:
      b3 = b12.get(True, None)
      b6 = b3.split(" ")
      b7 = b6[0]
      b8 = b6[1]
      b9 = " ".join(b6[2:])
      if (b9 != ""):
        for cID in b11:
          if cID != b7:
            b10 = b8 + " " + b7 + " " + b9 + "\n"
            b11[cID].send(b10.encode())
      b12.task_done()
  b11 = dict()
  a3 = 0
  b12 = Queue(100)
  threading.Thread(b13 = serverThread, args = (b11, b12)).start()
  b14 = ["Player1", "Player2"]
  while True:
    try:
      client, b15 = b2.accept()
      b16 = b14[a3]
      for cID in b11:
        b11[cID].send(("PlayerJoined %s\n" % b16).encode())
        client.send(("PlayerJoined %s\n" % cID).encode())
      b11[b16] = client
      client.send(("MyIDis %s \n" % b16).encode())
      print("Connection recieved from %s" % b16)
      threading.Thread(b13 = handleClient, args =
                            (client ,b12, b16, b11)).start()
      a3 += 1
    except:
      print("Max players reached")
if b17 = = '__main__': fonk1()