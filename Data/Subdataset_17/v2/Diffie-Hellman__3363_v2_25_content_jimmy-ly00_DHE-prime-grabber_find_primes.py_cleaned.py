import sys
import os
import subprocess
import re
import csv
def extract_dh_prime(cmd_output):
    for line in cmd_output.splitlines():
        if 'dh_p' in line:
            prime_hex = re.sub(".*: ", "", line)
            return int(prime_hex, 16)
    return None
def check_server_for_dh(server, servername, openssl_trace_path, cipher, port):
    try:
        cmd = subprocess.check_output(
            [openssl_trace_path, "s_client", "-trace", "-cipher", cipher, "-connect", f"{server}:{port}"],
            stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1
        )
        prime = extract_dh_prime(cmd.decode("ISO-8859-1"))
        if prime:
            return (server, servername, prime)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    return None
def main():
    input_file = 'alexa_top1mil'
    output_file = 'output.csv'
    openssl_trace_path = os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace")
    cipher = "DHE"
    port = "443"
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                server = row[0]
                servername = row[1]
                result = check_server_for_dh(server, servername, openssl_trace_path, cipher, port)
                if result:
                    writer.writerow(result)
if __name__ == "__main__":
    main()