import os
import fnmatch
import logging
b1 = "/path/to/wowza/recording/dir"
b2 = [
    "*_240p*.mp4",
    "*_360p*.mp4",
    "*_480p*.mp4",
    "*_720p*.mp4",
    "*_1080p*.mp4"
]
b3 = '/var/log/wowza_delete_recordings.log'
logging.basicConfig(b4 = '%(asctime)s %(message)s',
                    b5 = b3,
                    b6 = logging.INFO)
def fonk1(path, patterns):
    b7 = []
    for root, _, filenames in os.walk(path):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                b7.append(os.path.join(root, name))
    return b7
def fonk2(file_list):
    if not file_list:
        logging.info("Nothing to delete")
    else:
        for file_path in file_list:
            try:
                os.remove(file_path)
                logging.info("Deleted file: %s", file_path)
            except OSError as e:
                logging.error("Error deleting file %s: %s", file_path, e)
def fonk3():
    logging.info("Script started")
    b7 = fonk1(b1, b2)
    fonk2(b7)
    logging.info("Script ended")
if b8 = = "__main__":
    fonk3()