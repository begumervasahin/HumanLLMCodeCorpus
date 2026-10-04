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
def fonk2(b13, b14, b7, b8, b9):
    try:
        b2 = subprocess.check_output(
            [b7, "s_client", "-trace", "-b8", b8, "-connect", f"{b13}:{b9}"],
            b3 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1
        )
        b4 = fonk1(b2.decode("ISO-8859-1"))
        if b4:
            return (b13, b14, b4)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    return None
def fonk3():
    b5 = 'alexa_top1mil'
    b6 = 'output.csv'
    b7 = os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace")
    b8 = "DHE"
    b9 = "443"
    with open(b6, 'w', b10 = '') as outfile:
        b11 = csv.b11(outfile)
        with open(b5, 'r') as csvfile:
            b12 = csv.b12(csvfile, delimiter=',')
            for row in b12:
                b13 = row[0]
                b14 = row[1]
                b15 = fonk2(b13, b14, b7, b8, b9)
                if b15:
                    b11.writerow(b15)
if b16 = = "__main__":
    fonk3()