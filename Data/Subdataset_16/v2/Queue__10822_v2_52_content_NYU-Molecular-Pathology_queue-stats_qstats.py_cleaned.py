import datetime
import json
import os
import util.slurm as slurm
def fonk1():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
def fonk2():
    return "slurm.json", "slurm.json.tmp"
def fonk3():
    return {
        'best_queue': "intellispace",
        'intellispace_cpus': 0,
        'intellispace_cpus_limit': 160,
        'partition_blacklist': [
            "data_mover",
            "cpu_dev",
            "gpu4_dev",
            "gpu8_dev",
            "fn_long"
        ]
    }
def fonk4():
    return slurm.Partitions(), slurm.Squeue()
def fonk5(partitions, b8, b7, b5, output_json_file, b6):
    b1 = partitions.most_idle_nodes(blacklist=b7['partition_blacklist'])
    b2 = partitions.most_mixed_nodes(blacklist=b7['partition_blacklist'])
    for entry in b8.entries:
        if entry['PARTITION'] == 'intellispace':
            b7['intellispace_cpus'] += int(entry['CPUS'])
    if b7['intellispace_cpus'] < b7['intellispace_cpus_limit']:
        b7['best_queue'] = 'intellispace'
    elif b1:
        b7['best_queue'] = b1
    elif b2:
        b7['best_queue'] = b2
    print(f"[{b5}] best queue: {b7['best_queue']}, most idle: {b1}, most mixed: {b2}, intellispace cpus: {b7['intellispace_cpus']}")
    b3 = {
        'updated': b5,
        'b1': b1,
        'b2': b2,
        'intellispace_cpus': b7['intellispace_cpus'],
        'best_queue': b7['best_queue']
    }
    with open(b6, 'w') as f:
        json.dump(b3, f, b4 = 4)
    os.rename(b6, output_json_file)
def fonk6():
    b5 = fonk1()
    output_json_file, b6 = fonk2()
    b7 = fonk3()
    partitions, b8 = fonk4()
    if partitions.sinfo.b9 = = 0 and b8.b9 == 0:
        fonk5(partitions, b8, b7, b5, output_json_file, b6)
    else:
        print(f"[{b5}] error: SLURM command returned invalid exit status; sinfo code: {partitions.sinfo.b9}, b8 code: {b8.b9}")
if b10 = = '__main__':
    fonk6()