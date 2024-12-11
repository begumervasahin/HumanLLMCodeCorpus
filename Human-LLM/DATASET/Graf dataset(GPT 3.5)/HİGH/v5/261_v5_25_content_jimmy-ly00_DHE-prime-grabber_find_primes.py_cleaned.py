import sys
import os
import subprocess
import re
import csv
def fonk1(server, b7):
    try:
        b1 = subprocess.check_output([
            os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace"),
            "s_client", "-trace",
            "-cipher", "DHE",
            "-connect", f"{server}:443"
        ],
        b2 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
        for line in b1.decode("ISO-8859-1").splitlines():
            if 'dh_p' in line:
                b3 = int(re.sub(".*: ", "", line), 16)
                return b3
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
def fonk2():
    with open('output.csv', 'w', b4 = '') as outfile:
        b5 = csv.writer(outfile)
        with open('alexa_top1mil.csv', 'r') as csvfile:
            b6 = csv.b6(csvfile, delimiter=',')
            for row in b6:
                server, b7 = row[:2]
                b3 = fonk1(server, b7)
                if b3 is not None:
                    b5.writerow([server, b7, b3])
if b8 = = "__main__":
    fonk2()