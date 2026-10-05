import os
import fnmatch
import logging
WOWZA_RECORDING_PATH = "/path/to/wowza/recording/dir"
EXCESSIVE_RECORDING_PATTERNS = ["*_240p*.mp4", "*_360p*.mp4", "*_480p*.mp4", "*_720p*.mp4", "*_1080p*.mp4"]
LOG_FILE_PATH = '/var/log/wowza_delete_recordings.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILE_PATH, level=logging.INFO)
def delete_excessive_recordings(directory, patterns):
    files_to_delete = []
    for root, _, filenames in os.walk(directory):
        for pattern in patterns:
            for filename in fnmatch.filter(filenames, pattern):
                files_to_delete.append(os.path.join(root, filename))
    if not files_to_delete:
        logging.info("No excessive recordings found.")
    else:
        for file_path in files_to_delete:
            os.remove(file_path)
            logging.info("Deleted file: %s", file_path)
    logging.info("Script execution completed.")
if __name__ == "__main__":
    delete_excessive_recordings(WOWZA_RECORDING_PATH, EXCESSIVE_RECORDING_PATTERNS)