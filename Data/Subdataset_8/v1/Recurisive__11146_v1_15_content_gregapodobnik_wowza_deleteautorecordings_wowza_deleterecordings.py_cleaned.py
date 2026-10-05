import os
import fnmatch
import logging
PATH = "/path/to/wowza/recording/dir"
DELPATTERN = ["*_240p*.mp4",
              "*_360p*.mp4",
              "*_480p*.mp4",
              "*_720p*.mp4",
              "*_1080p*.mp4"]
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='/var/log/wowza_delete_recordings.log',
                    level=logging.INFO)
logging.info("Script started")
def delete_excessive_recordings(path, patterns):
    files_to_delete = []
    for root, dirs, filenames in os.walk(path):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                files_to_delete.append(os.path.join(root, name))
    if not files_to_delete:
        logging.info("Nothing to delete")
    else:
        for deleted in files_to_delete:
            os.remove(deleted)
            logging.info("Deleted file : %s", deleted)
    logging.info("Script ended")
if __name__ == "__main__":
    delete_excessive_recordings(PATH, DELPATTERN)