import sys, os, subprocess, re, csv
outfile = open('output.csv', 'w')
wr = csv.writer(outfile)
with open('alexa_top1mil', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        server = row[0]
        servername = row[1]
        try:
            cmd = subprocess.check_output([os.path.dirname(sys.argv[0])+"/openssl-trace",
                "s_client", "-trace",
                "-cipher", "DHE",
                "-connect", server+":443"],
                stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
            for line in cmd.decode("ISO-8859-1").splitlines():
                if 'dh_p' in line:
                    prime = int(re.sub(".*: ", "", line), 16)
                    wr.writerow([server, servername, prime])
        except subprocess.CalledProcessError:
            pass
        except subprocess.TimeoutExpired:
            pass