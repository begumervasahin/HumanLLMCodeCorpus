import util.slurm as slurm
import datetime
import json
import os
timestamp = datetime.datetime.now()
timestamp_str = timestamp.strftime('%Y-%m-%dT%H:%M:%S')
output_json_file = "slurm.json"
output_json_file_tmp = "slurm.json.tmp"
best_queue = "intellispace"
intellispace_cpus = 0
intellispace_cpus_limit = 160
partition_blacklist = [
    "data_mover",
    "cpu_dev",
    "gpu4_dev",
    "gpu8_dev",
    "fn_long"
]
partitions = slurm.Partitions()
squeue = slurm.Squeue()
def get_best_queue():
    most_idle = partitions.most_idle_nodes(blacklist=partition_blacklist)
    most_mixed = partitions.most_mixed_nodes(blacklist=partition_blacklist)
    for entry in squeue.entries:
        if entry['PARTITION'] == 'intellispace':
            intellispace_cpus += int(entry['CPUS'])
    if intellispace_cpus < intellispace_cpus_limit:
        best_queue = 'intellispace'
    elif most_idle:
        best_queue = most_idle
    elif most_mixed:
        best_queue = most_mixed
    print("[{timestamp}] best queue: {best_queue}, most idle: {most_idle}, most mixed: {most_mixed}, intellispace cpus: {intellispace_cpus}".format(
        timestamp=timestamp_str,
        best_queue=best_queue,
        most_idle=most_idle,
        most_mixed=most_mixed,
        intellispace_cpus=intellispace_cpus
    ))
    data = {
        'updated': timestamp_str,
        'most_idle': most_idle,
        'most_mixed': most_mixed,
        'intellispace_cpus': intellispace_cpus,
        'best_queue': best_queue
    }
    with open(output_json_file_tmp, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(output_json_file_tmp, output_json_file)
if partitions.sinfo.returncode == 0 and squeue.returncode == 0:
    get_best_queue()
else:
    print("[{timestamp}] error: SLURM command returned invalid exit status; sinfo code: {sinfo_code}, squeue code: {squeue_code}".format(
        timestamp=timestamp_str,
        sinfo_code=partitions.sinfo.returncode,
        squeue_code=squeue.returncode
    ))