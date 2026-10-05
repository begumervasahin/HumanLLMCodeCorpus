import socket
import sys
def run_udp_server(udp_ip, udp_port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        udp_socket.bind((udp_ip, udp_port))
        print(f"UDP server is listening on {udp_ip}:{udp_port}")
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print("Received message:", data.decode('utf-8'))
    except OSError as e:
        print(f"Error binding UDP socket: {e}")
    finally:
        udp_socket.close()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python udp_server.py <UDP_PORT>")
        sys.exit(1)
    udp_port = int(sys.argv[1])
    udp_ip = "160.39.231.6"
    run_udp_server(udp_ip, udp_port)