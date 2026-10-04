import socket
import sys
import pickle
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    recvsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recvsock.bind(("", port))
    print(f"Listening on port {port}")
    data, addr = recvsock.recvfrom(4096)
    recovered = pickle.loads(data)
    print(f"Sender: {addr}")
    print(f"Recovered entry: {recovered}")
if __name__ == "__main__":
    main()