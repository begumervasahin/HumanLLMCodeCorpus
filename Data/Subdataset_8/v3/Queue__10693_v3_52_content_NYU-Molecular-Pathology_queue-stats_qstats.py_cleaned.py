import datetime
import json
import os
import util.slurm as slurm
timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
output_json_file = "slurm.json"
output_json_file_tmp = "slurm.json.tmp"
best_queue = "intellispace"
intellispace_cpus_limit = 160
partition_blacklist = [
    "data_mover",
    "cpu_dev",
    "gpu4_dev",
    "gpu8_dev",
    "fn_long"
]
def get_best_queue(partitions, squeue, intellispace_cpus_limit, partition_blacklist, timestamp, output_json_file, best_queue):
    most_idle = partitions.most_idle_nodes(blacklist=partition_blacklist)
    most_mixed = partitions.most_mixed_nodes(blacklist=partition_blacklist)
    intellispace_cpus = sum(int(entry['CPUS']) for entry in squeue.entries if entry['PARTITION'] == 'intellispace')
    if intellispace_cpus < intellispace_cpus_limit:
        best_queue = 'intellispace'
    elif most_idle:
        best_queue = most_idle
    elif most_mixed:
        best_queue = most_mixed
    data = {
        'updated': timestamp,
        'most_idle': most_idle,
        'most_mixed': most_mixed,
        'intellispace_cpus': intellispace_cpus,
        'best_queue': best_queue
    }
    with open(output_json_file_tmp, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(output_json_file_tmp, output_json_file)
partitions = slurm.Partitions()
squeue = slurm.Squeue()
if partitions.sinfo.returncode == 0 and squeue.returncode == 0:
    get_best_queue(partitions, squeue, intellispace_cpus_limit, partition_blacklist, timestamp, output_json_file, best_queue)
else:
    sinfo_code = partitions.sinfo.returncode
    squeue_code = squeue.returncode
    print(f"[{timestamp}] error: SLURM command returned invalid exit status; sinfo code: {sinfo_code}, squeue code: {squeue_code}")