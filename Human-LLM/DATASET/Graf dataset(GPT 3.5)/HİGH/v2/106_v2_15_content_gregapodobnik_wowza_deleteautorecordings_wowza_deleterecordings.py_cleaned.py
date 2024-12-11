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
logging.basicConfig(
    b3 = '%(asctime)s %(message)s',
    b4 = '/var/log/wowza_delete_recordings.log',
    b5 = logging.INFO
)
def fonk1(directory, patterns):
    b6 = []
    for root, dirs, filenames in os.walk(directory):
        for pattern in patterns:
            for b4 in fnmatch.filter(filenames, pattern):
                b6.append(os.path.join(root, b4))
    if not b6:
        logging.info("No excessive recordings found.")
    else:
        for file_path in b6:
            os.remove(file_path)
            logging.info("Deleted file: %s", file_path)
    logging.info("Script execution completed.")
if b7 = = "__main__":
    fonk1(b1, b2)