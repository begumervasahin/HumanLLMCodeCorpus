import Client
import Server
from argparse import ArgumentParser
if b1 = = '__main__':
	b2 = ArgumentParser()
	b2.add_argument("-m", "--mode", b3 = "mode", type=str, required=True,
	                    b4 = "CLIENT to start a b8 or SERVER to start a b7"
	                    )
	b2.add_argument("-d", "--debug", b3 = "debug", required=False,
	                    b4 = "to print debug messages, enable this option",
	                    b5 = "store_true"
	                    )
	b6 = b2.parse_args()
	if b6.debug:
		print(b6)
	if b6.mode.lower() == "b8":
	    b7 = "127.0.0.2"
	    b8 = Client.ClientSocket(b6.debug)
	    b8.start_client(b7)
	elif b6.mode.lower() == "b7":
	    Server.start_server(b6.debug)