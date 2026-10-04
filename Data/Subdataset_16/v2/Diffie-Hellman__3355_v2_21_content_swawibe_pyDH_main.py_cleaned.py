import Client
import Server
from argparse import ArgumentParser
def fonk1():
    b1 = ArgumentParser(description="Start a b8 or server for network communication.")
    b1.add_argument("-m", "--b6", b2 = str, required=True,
                        b3 = "Specify 'b8' to start a b8 or 'server' to start a server")
    b1.add_argument("-d", "--b9", b4 = "store_true", required=False,
                        b3 = "Enable b9 b6 to print b9 messages")
    return b1.parse_args()
def fonk2():
    b5 = fonk1()
    if b5.b9:
        print("Arguments:", b5)
    b6 = b5.b6.lower()
    if b6 = = "b8":
        b7 = "127.0.0.2"
        b8 = Client.ClientSocket(b9=b5.b9)
        b8.start_client(b7)
    elif b6 = = "server":
        Server.start_server(b9 = b5.b9)
    else:
        print("Invalid b6. Please specify 'b8' or 'server'.")
if b10 = = "__main__":
    fonk2()