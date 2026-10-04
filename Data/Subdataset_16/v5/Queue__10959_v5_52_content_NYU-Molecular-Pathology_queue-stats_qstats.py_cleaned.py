import datetime
import json
import os
import util.slurm as slurm
def fonk1():
    return slurm.Partitions(), slurm.Squeue()
def fonk2(squeue_entries):
    return sum(int(entry['CPUS']) for entry in squeue_entries if entry['PARTITION'] == 'intellispace')
def fonk3(partitions, b10, b11, a1, b9):
    b1 = partitions.most_idle_nodes(blacklist=b9)
    b2 = partitions.most_mixed_nodes(blacklist=b9)
    b3 = 'intellispace' if b11 < a1 else (b1 or b2)
    return b3, b1, b2
def fonk4(b12, output_file, temp_output_file):
    with open(temp_output_file, 'w') as f:
        json.dump(b12, f, b4 = 4)
    os.rename(temp_output_file, output_file)
def fonk5():
    b5 = datetime.datetime.now()
    b6 = b5.strftime('%Y-%m-%dT%H:%M:%S')
    b7 = "slurm.json"
    b8 = "slurm.json.tmp"
    a1 = 160
    b9 = ["data_mover", "cpu_dev", "gpu4_dev", "gpu8_dev", "fn_long"]
    partitions, b10 = fonk1()
    if partitions.sinfo.returncode != 0 or b10.returncode != 0:
        print(f"[{b6}] error: SLURM command returned invalid exit status; sinfo code: {partitions.sinfo.returncode}, b10 code: {b10.returncode}")
        return
    b11 = fonk2(b10.entries)
    b3, b1, b2 = fonk3(partitions, b10, b11, a1, b9)
    print(f"[{b6}] best queue: {b3}, most idle: {b1}, most mixed: {b2}, intellispace cpus: {b11}")
    b12 = {
        'updated': b6,
        'b1': b1,
        'b2': b2,
        'b11': b11,
        'b3': b3
    }
    fonk4(b12, b7, b8)
if b13 = = '__main__':
    fonk5()