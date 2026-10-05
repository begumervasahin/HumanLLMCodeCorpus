import paderson_commitment
import os
import random
from datetime import datetime
from threading import Thread
class NodeA(Thread):
    def run(self):
        os.system('sleep 0.1; python3 node-A.py')
class NodeB(Thread):
    def run(self):
        os.system('python3 node-B.py')
def update_constants_file(port, shared_prime, random_length, prime_length):
    with open('constants.py', 'w') as constants_file:
        constants_file.write('PORT = {}\n'.format(port))
        constants_file.write('SERVER_IP_ADDR = "127.0.0.1"\n')
        constants_file.write('SHARED_PRIME = {}\n'.format(shared_prime))
        constants_file.write('SHARED_BASE = 2\n')
        constants_file.write('RANDOM_STRING_LENGTH = {}\n'.format(random_length))
        constants_file.write('RAND_NUMBER_LOWER_BOUND = 100\n')
        constants_file.write('RAND_NUMBER_UPPER_BOUND = 1000\n')
        constants_file.write('LENGTH_OF_PRIME = {}\n'.format(prime_length))
def main():
    random_lengths = list(range(10, 100, 5))
    prime_lengths = [100, 140, 160, 180, 320, 384, 512]
    with open('funny1.csv', 'a') as csvfile:
        for prime_length in prime_lengths:
            paderson_commitment.generate_p_g_q()
            with open('constants.py', 'w') as constants_file:
                constants_file.write("LENGTH_OF_PRIME = {}\n".format(prime_length))
            for random_length in random_lengths:
                port = random.randint(13000, 20000)
                shared_prime = paderson_commitment.get_shared_prime()
                update_constants_file(port, shared_prime, random_length, prime_length)
                os.system('sleep 1')
                node_b = NodeB()
                node_a = NodeA()
                start_time = datetime.now()
                node_b.start()
                node_a.start()
                node_a.join()
                node_b.join()
                end_time = datetime.now()
                execution_time = (end_time - start_time).microseconds
                csv_data = "{},{},{}\n".format(prime_length, random_length, execution_time)
                csvfile.write(csv_data)
                csvfile.flush()
if __name__ == "__main__":
    main()