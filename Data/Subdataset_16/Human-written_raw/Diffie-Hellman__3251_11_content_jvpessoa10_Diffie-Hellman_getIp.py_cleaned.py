import os
import socket
if os.name != "nt":
    import fcntl
    import struct
    def fonk1(ifname):
        b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(b1.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])
def fonk2():
    b2 = socket.gethostbyname(socket.gethostname())
    if b2.startswith("127.") and os.name != "nt":
        b3 = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in b3:
            try:
                b2 = fonk1(ifname)
                break
            except IOError:
                pass
    return b2