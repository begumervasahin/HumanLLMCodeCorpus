import socket
import sys
import pickle
def receive_data(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as recvsock:
        recvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        recvsock.bind(("", port))
        print(f"Listening on port {port}")
        data, addr = recvsock.recvfrom(4096)
    return data, addr
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    data, addr = receive_data(port)
    recovered = pickle.loads(data)
    print(f"Sender: {addr}")
    print(f"Recovered entry: {recovered}")
if __name__ == "__main__":
    main()