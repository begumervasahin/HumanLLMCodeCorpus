import os
import fnmatch
import logging
def delete_matching_files(directory, patterns):
    deleted_files = []
    for root, _, filenames in os.walk(directory):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                file_path = os.path.join(root, name)
                os.remove(file_path)
                deleted_files.append(file_path)
    return deleted_files
def setup_logging(log_file):
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename=log_file,
                        level=logging.INFO)
def main():
    recording_directory = "/path/to/wowza/recording/dir"
    deletion_patterns = ["*_240p*.mp4",
                         "*_360p*.mp4",
                         "*_480p*.mp4",
                         "*_720p*.mp4",
                         "*_1080p*.mp4"]
    log_file = '/var/log/wowza_delete_recordings.log'
    setup_logging(log_file)
    logging.info("Script started")
    deleted_files = delete_matching_files(recording_directory, deletion_patterns)
    if not deleted_files:
        logging.info("Nothing to delete")
    else:
        for deleted_file in deleted_files:
            logging.info("Deleted file: %s", deleted_file)
    logging.info("Script ended")
if __name__ == "__main__":
    main()