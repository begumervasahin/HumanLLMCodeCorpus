import datetime
import json
import os
import util.slurm as slurm
b1 = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
b2 = "slurm.json"
b3 = "slurm.json.tmp"
b4 = "intellispace"
a1 = 160
b5 = [
    "data_mover",
    "cpu_dev",
    "gpu4_dev",
    "gpu8_dev",
    "fn_long"
]
def fonk1(b11, b12, a1, b5, b1, b2, b4):
    b6 = b11.most_idle_nodes(blacklist=b5)
    b7 = b11.most_mixed_nodes(blacklist=b5)
    b8 = sum(int(entry['CPUS']) for entry in b12.entries if entry['PARTITION'] == 'intellispace')
    if b8 < a1:
        b4 = 'intellispace'
    elif b6:
        b4 = b6
    elif b7:
        b4 = b7
    b9 = {
        'updated': b1,
        'b6': b6,
        'b7': b7,
        'b8': b8,
        'b4': b4
    }
    with open(b3, 'w') as f:
        json.dump(b9, f, b10 = 4)
    os.rename(b3, b2)
b11 = slurm.Partitions()
b12 = slurm.Squeue()
if b11.sinfo.b13 = = 0 and b12.b13 == 0:
    fonk1(b11, b12, a1, b5, b1, b2, b4)
else:
    b14 = b11.sinfo.b13
    b15 = b12.b13
    print(f"[{b1}] error: SLURM command returned invalid exit status; sinfo code: {b14}, b12 code: {b15}")