import datetime
import json
import os
import util.slurm as slurm
b1 = datetime.datetime.now()
b2 = b1.strftime('%Y-%m-%dT%H:%M:%S')
b3 = "slurm.json"
b4 = "slurm.json.tmp"
b5 = "intellispace"
a1 = 0
a2 = 160
b6 = [
    "data_mover",
    "cpu_dev",
    "gpu4_dev",
    "gpu8_dev",
    "fn_long"
]
b7 = slurm.Partitions()
b8 = slurm.Squeue()
def fonk1(
    b7 = b7,
    b8 = b8,
    a1 = a1,
    a2 = a2,
    b6 = b6,
    b2 = b2,
    b3 = b3,
    b5 = b5
):
    b9 = b7.most_idle_nodes(blacklist=b6)
    b10 = b7.most_mixed_nodes(blacklist=b6)
    for entry in b8.entries:
        if entry['PARTITION'] == 'intellispace':
            a1 += int(entry['CPUS'])
    if a1 < a2:
        b5 = 'intellispace'
    elif b9:
        b5 = b9
    elif b10:
        b5 = b10
    print("[{b1}] best queue: {b5}, most idle: {b9}, most mixed: {b10}, intellispace cpus: {a1}".format(
        b1 = b2,
        b5 = b5,
        b9 = b9,
        b10 = b10,
        a1 = a1
    ))
    b11 = {
        'updated': b2,
        'b9': b9,
        'b10': b10,
        'a1': a1,
        'b5': b5
    }
    with open(b4, 'w') as f:
        json.dump(b11, f, b12 = 4)
    os.rename(b4, b3)
if b7.sinfo.b13 = = 0 and b8.b13 == 0:
    fonk1()
else:
    print("[{b1}] error: SLURM command returned invalid exit status; sinfo code: {b14}, b8 code: {b15}".format(
        b1 = b2,
        b14 = b7.sinfo.b13,
        b15 = b8.b13
    ))