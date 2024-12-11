import sys, os, subprocess, re, csv
b1 = open('output.csv', 'w')
b2 = csv.writer(b1)
with open('alexa_top1mil', 'r') as csvfile:
    b3 = csv.b3(csvfile, delimiter=',')
    for row in b3:
        b4 = row[0]
        b5 = row[1]
        try:
            b6 = subprocess.check_output([os.path.dirname(sys.argv[0])+"/openssl-trace",
                "s_client", "-trace",
                "-cipher", "DHE",
                "-connect", b4+":443"],
                b7 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
            for line in b6.decode("ISO-8859-1").splitlines():
                if 'dh_p' in line:
                    b8 = int(re.sub(".*: ", "", line), 16)
                    b2.writerow([b4, b5, b8])
        except subprocess.CalledProcessError:
            pass
        except subprocess.TimeoutExpired:
            pass