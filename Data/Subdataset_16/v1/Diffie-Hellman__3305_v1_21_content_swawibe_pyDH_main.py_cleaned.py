import Client
import Server
from argparse import ArgumentParser
def fonk1():
    b1 = ArgumentParser(description="Start a b6 or server for network communication.")
    b1.add_argument("-m", "--mode", b2 = "mode", type=str, required=True,
                        b3 = "Specify 'CLIENT' to start a b6 or 'SERVER' to start a server")
    b1.add_argument("-d", "--b7", b2 = "b7", action="store_true", required=False,
                        b3 = "Enable b7 mode to print b7 messages")
    b4 = b1.parse_args()
    if b4.b7:
        print("Arguments:", b4)
    if b4.mode.lower() == "b6":
        b5 = "127.0.0.2"
        b6 = Client.ClientSocket(b7=b4.b7)
        b6.start_client(b5)
    elif b4.mode.lower() == "server":
        Server.start_server(b7 = b4.b7)
    else:
        print("Invalid mode. Please specify 'CLIENT' or 'SERVER'.")
if b8 = = "__main__":
    fonk1()