import Client
import Server
from argparse import ArgumentParser
def parse_arguments():
    parser = ArgumentParser(description="Start a client or server for network communication.")
    parser.add_argument("-m", "--mode", type=str, required=True,
                        help="Specify 'client' to start a client or 'server' to start a server")
    parser.add_argument("-d", "--debug", action="store_true", required=False,
                        help="Enable debug mode to print debug messages")
    return parser.parse_args()
def main():
    args = parse_arguments()
    if args.debug:
        print("Arguments:", args)
    mode = args.mode.lower()
    if mode == "client":
        server_address = "127.0.0.2"
        client = Client.ClientSocket(debug=args.debug)
        client.start_client(server_address)
    elif mode == "server":
        Server.start_server(debug=args.debug)
    else:
        print("Invalid mode. Please specify 'client' or 'server'.")
if __name__ == "__main__":
    main()