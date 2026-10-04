import sys
import os
import subprocess
import re
import csv
def fonk1():
    b1 = 'alexa_top1mil'
    b2 = 'output.csv'
    b3 = os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace")
    b4 = "DHE"
    b5 = "443"
    with open(b2, 'w', b6 = '') as outfile:
        b7 = csv.b7(outfile)
        with open(b1, 'r') as csvfile:
            b8 = csv.b8(csvfile, delimiter=',')
            for row in b8:
                b9 = row[0]
                b10 = row[1]
                try:
                    b11 = subprocess.check_output(
                        [b3, "s_client", "-trace", "-b4", b4, "-connect", f"{b9}:{b5}"],
                        b12 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1
                    )
                    for line in b11.decode("ISO-8859-1").splitlines():
                        if 'dh_p' in line:
                            b13 = int(re.sub(".*: ", "", line), 16)
                            b7.writerow([b9, b10, b13])
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                    pass
if b14 = = "__main__":
    fonk1()