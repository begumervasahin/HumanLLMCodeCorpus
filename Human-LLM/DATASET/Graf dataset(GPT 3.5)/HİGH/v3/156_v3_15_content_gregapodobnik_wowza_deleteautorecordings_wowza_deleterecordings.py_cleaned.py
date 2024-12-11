import os
import fnmatch
import logging
b1 = "/path/to/wowza/recording/dir"
b2 = ["*_240p*.mp4", "*_360p*.mp4", "*_480p*.mp4", "*_720p*.mp4", "*_1080p*.mp4"]
b3 = '/var/log/wowza_delete_recordings.log'
logging.basicConfig(b4 = '%(asctime)s %(message)s', filename=b3, level=logging.INFO)
def fonk1(directory, patterns):
    b5 = []
    for root, _, filenames in os.walk(directory):
        for pattern in patterns:
            for filename in fnmatch.filter(filenames, pattern):
                b5.append(os.path.join(root, filename))
    if not b5:
        logging.info("No excessive recordings found.")
    else:
        for file_path in b5:
            os.remove(file_path)
            logging.info("Deleted file: %s", file_path)
    logging.info("Script execution completed.")
if b6 = = "__main__":
    fonk1(b1, b2)