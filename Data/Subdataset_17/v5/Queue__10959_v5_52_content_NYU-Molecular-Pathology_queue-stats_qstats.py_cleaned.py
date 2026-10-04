import datetime
import json
import os
import util.slurm as slurm
def fetch_slurm_info():
    return slurm.Partitions(), slurm.Squeue()
def calculate_intellispace_cpus(squeue_entries):
    return sum(int(entry['CPUS']) for entry in squeue_entries if entry['PARTITION'] == 'intellispace')
def determine_best_queue(partitions, squeue, intellispace_cpus, intellispace_cpus_limit, partition_blacklist):
    most_idle = partitions.most_idle_nodes(blacklist=partition_blacklist)
    most_mixed = partitions.most_mixed_nodes(blacklist=partition_blacklist)
    best_queue = 'intellispace' if intellispace_cpus < intellispace_cpus_limit else (most_idle or most_mixed)
    return best_queue, most_idle, most_mixed
def save_to_json(data, output_file, temp_output_file):
    with open(temp_output_file, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(temp_output_file, output_file)
def main():
    timestamp = datetime.datetime.now()
    timestamp_str = timestamp.strftime('%Y-%m-%dT%H:%M:%S')
    output_json_file = "slurm.json"
    output_json_file_tmp = "slurm.json.tmp"
    intellispace_cpus_limit = 160
    partition_blacklist = ["data_mover", "cpu_dev", "gpu4_dev", "gpu8_dev", "fn_long"]
    partitions, squeue = fetch_slurm_info()
    if partitions.sinfo.returncode != 0 or squeue.returncode != 0:
        print(f"[{timestamp_str}] error: SLURM command returned invalid exit status; sinfo code: {partitions.sinfo.returncode}, squeue code: {squeue.returncode}")
        return
    intellispace_cpus = calculate_intellispace_cpus(squeue.entries)
    best_queue, most_idle, most_mixed = determine_best_queue(partitions, squeue, intellispace_cpus, intellispace_cpus_limit, partition_blacklist)
    print(f"[{timestamp_str}] best queue: {best_queue}, most idle: {most_idle}, most mixed: {most_mixed}, intellispace cpus: {intellispace_cpus}")
    data = {
        'updated': timestamp_str,
        'most_idle': most_idle,
        'most_mixed': most_mixed,
        'intellispace_cpus': intellispace_cpus,
        'best_queue': best_queue
    }
    save_to_json(data, output_json_file, output_json_file_tmp)
if __name__ == '__main__':
    main()