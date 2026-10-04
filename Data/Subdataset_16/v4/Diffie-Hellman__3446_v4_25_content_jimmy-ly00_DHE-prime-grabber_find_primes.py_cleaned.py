import sys
import os
import subprocess
import re
import csv
def fonk1(cmd_output):
    for line in cmd_output.splitlines():
        if 'dh_p' in line:
            b1 = re.sub(".*: ", "", line)
            return int(b1, 16)
    return None
def fonk2(server, b8, b12):
    try:
        b2 = subprocess.check_output(
            [b12, "s_client", "-trace", "-cipher", "DHE", "-connect", f"{server}:443"],
            b3 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1
        )
        b4 = fonk1(b2.decode("ISO-8859-1"))
        if b4:
            return (server, b8, b4)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    return None
def fonk3(b10, b11, b12):
    with open(b11, 'w', b5 = '') as outfile:
        b6 = csv.b6(outfile)
        with open(b10, 'r') as csvfile:
            b7 = csv.b7(csvfile, delimiter=',')
            for row in b7:
                server, b8 = row[0], row[1]
                b9 = fonk2(server, b8, b12)
                if b9:
                    b6.writerow(b9)
def fonk4():
    b10 = 'alexa_top1mil'
    b11 = 'output.csv'
    b12 = os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace")
    fonk3(b10, b11, b12)
if b13 = = "__main__":
    fonk4()