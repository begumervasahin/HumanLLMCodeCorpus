import datetime
import json
import os
import util.slurm as slurm
def get_current_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
def initialize_output_files():
    return "slurm.json", "slurm.json.tmp"
def initialize_settings():
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
def fetch_slurm_info():
    return slurm.Partitions(), slurm.Squeue()
def get_best_queue(partitions, squeue, settings, timestamp_str, output_json_file, output_json_file_tmp):
    most_idle = partitions.most_idle_nodes(blacklist=settings['partition_blacklist'])
    most_mixed = partitions.most_mixed_nodes(blacklist=settings['partition_blacklist'])
    for entry in squeue.entries:
        if entry['PARTITION'] == 'intellispace':
            settings['intellispace_cpus'] += int(entry['CPUS'])
    if settings['intellispace_cpus'] < settings['intellispace_cpus_limit']:
        settings['best_queue'] = 'intellispace'
    elif most_idle:
        settings['best_queue'] = most_idle
    elif most_mixed:
        settings['best_queue'] = most_mixed
    print(f"[{timestamp_str}] best queue: {settings['best_queue']}, most idle: {most_idle}, most mixed: {most_mixed}, intellispace cpus: {settings['intellispace_cpus']}")
    data = {
        'updated': timestamp_str,
        'most_idle': most_idle,
        'most_mixed': most_mixed,
        'intellispace_cpus': settings['intellispace_cpus'],
        'best_queue': settings['best_queue']
    }
    with open(output_json_file_tmp, 'w') as f:
        json.dump(data, f, indent=4)
    os.rename(output_json_file_tmp, output_json_file)
def main():
    timestamp_str = get_current_timestamp()
    output_json_file, output_json_file_tmp = initialize_output_files()
    settings = initialize_settings()
    partitions, squeue = fetch_slurm_info()
    if partitions.sinfo.returncode == 0 and squeue.returncode == 0:
        get_best_queue(partitions, squeue, settings, timestamp_str, output_json_file, output_json_file_tmp)
    else:
        print(f"[{timestamp_str}] error: SLURM command returned invalid exit status; sinfo code: {partitions.sinfo.returncode}, squeue code: {squeue.returncode}")
if __name__ == '__main__':
    main()