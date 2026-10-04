import os
import fnmatch
import logging
RECORDING_PATH = "/path/to/wowza/recording/dir"
DELETE_PATTERNS = [
    "*_240p*.mp4",
    "*_360p*.mp4",
    "*_480p*.mp4",
    "*_720p*.mp4",
    "*_1080p*.mp4"
]
LOG_FILE = '/var/log/wowza_delete_recordings.log'
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename=LOG_FILE,
                    level=logging.INFO)
def find_files_to_delete(path, patterns):
    files_to_delete = []
    for root, _, filenames in os.walk(path):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                files_to_delete.append(os.path.join(root, name))
    return files_to_delete
def delete_files(file_list):
    if not file_list:
        logging.info("Nothing to delete")
    else:
        for file_path in file_list:
            os.remove(file_path)
            logging.info("Deleted file: %s", file_path)
def main():
    logging.info("Script started")
    files_to_delete = find_files_to_delete(RECORDING_PATH, DELETE_PATTERNS)
    delete_files(files_to_delete)
    logging.info("Script ended")
if __name__ == "__main__":
    main()