import Client
import Server
from argparse import ArgumentParser
def main():
    parser = ArgumentParser(description="Start a client or server for network communication.")
    parser.add_argument("-m", "--mode", dest="mode", type=str, required=True,
                        help="Specify 'CLIENT' to start a client or 'SERVER' to start a server")
    parser.add_argument("-d", "--debug", dest="debug", action="store_true", required=False,
                        help="Enable debug mode to print debug messages")
    args = parser.parse_args()
    if args.debug:
        print("Arguments:", args)
    if args.mode.lower() == "client":
        server_address = "127.0.0.2"
        client = Client.ClientSocket(debug=args.debug)
        client.start_client(server_address)
    elif args.mode.lower() == "server":
        Server.start_server(debug=args.debug)
    else:
        print("Invalid mode. Please specify 'CLIENT' or 'SERVER'.")
if __name__ == "__main__":
    main()