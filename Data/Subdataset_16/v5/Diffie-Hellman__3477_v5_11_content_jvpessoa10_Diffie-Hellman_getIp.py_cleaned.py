import os
import socket
if os.name != "nt":
    import fcntl
    import struct
    def fonk1(ifname):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            return socket.inet_ntoa(
                fcntl.ioctl(
                    s.fileno(),
                    0x8915,
                    struct.pack('256s', ifname[:15].encode('utf-8'))
                )[20:24]
            )
def fonk2():
    b1 = socket.gethostbyname(socket.gethostname())
    if b1.startswith("127.") and os.name != "nt":
        b2 = [
            "eth0", "eth1", "eth2",
            "wlan0", "wlan1",
            "wifi0",
            "ath0", "ath1",
            "ppp0"
        ]
        for ifname in b2:
            try:
                b1 = fonk1(ifname)
                if b1:
                    break
            except IOError:
                continue
    return b1
if b3 = = "__main__":
    b4 = fonk2()
    print(f"LAN IP Address: {b4}")