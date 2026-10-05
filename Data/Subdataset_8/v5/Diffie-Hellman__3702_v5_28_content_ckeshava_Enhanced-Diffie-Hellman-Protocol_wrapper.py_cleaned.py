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
def main():
    prime_lengths = [100, 140, 160, 180, 320, 384, 512]
    random_lengths = list(range(10, 100, 5))
    with open('funny1.csv', 'a') as csv_file:
        for prime_length in prime_lengths:
            update_constants('LENGTH_OF_PRIME', prime_length)
            p, _, _ = paderson_commitment.generate_p_g_q()
            for random_length in random_lengths:
                port = random.randint(13000, 20000)
                update_constants('PORT', port)
                update_constants('SHARED_PRIME', p)
                update_constants('RANDOM_STRING_LENGTH', random_length)
                os.system('sleep 1')
                start_time = datetime.now()
                run_nodes()
                end_time = datetime.now()
                execution_time = (end_time - start_time).microseconds
                write_to_csv(csv_file, prime_length, random_length, execution_time)
def update_constants(key, value):
    with open('constants.py', 'w') as constants_file:
        constants_file.write(f"{key} = {value}\n")
def run_nodes():
    node_b = NodeB()
    node_a = NodeA()
    node_b.start()
    node_a.start()
    node_a.join()
    node_b.join()
def write_to_csv(csv_file, prime_length, random_length, execution_time):
    csv_data = f"{prime_length},{random_length},{execution_time}\n"
    csv_file.write(csv_data)
    csv_file.flush()
if __name__ == "__main__":
    main()