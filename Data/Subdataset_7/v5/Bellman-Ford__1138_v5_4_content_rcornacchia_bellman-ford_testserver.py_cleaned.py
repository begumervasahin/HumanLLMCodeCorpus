import socket
import sys
def fonk1(b5, b4):
    b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        b1.bind((b5, b4))
        print(f"UDP server is listening on {b5}:{b4}")
        while True:
            data, b2 = b1.recvfrom(1024)
            print("Received message:", data.decode('utf-8'))
    except OSError as e:
        print(f"Error binding UDP socket: {e}")
    finally:
        b1.close()
if b3 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python udp_server.py <UDP_PORT>")
        sys.exit(1)
    b4 = int(sys.argv[1])
    b5 = "160.39.231.6"
    fonk1(b5, b4)