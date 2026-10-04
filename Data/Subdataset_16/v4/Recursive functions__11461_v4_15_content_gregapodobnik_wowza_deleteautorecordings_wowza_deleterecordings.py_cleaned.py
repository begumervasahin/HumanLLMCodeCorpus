"""
Description: Delete excessive recordings (240p, 360p,...) from Wowza autorecording function.
Usage: Recursively search input folder for "_240p", "_360p", "_480p", "_720p" and "_1080p"
filenames and delete them. Script should be used with cronjob or similar tool.
Before running, define correct path and pattern of files to be deleted.
"""
import os
import fnmatch
import logging
b1 = "/path/to/wowza/recording/dir"
b2 = ["*_240p*.mp4",
              "*_360p*.mp4",
              "*_480p*.mp4",
              "*_720p*.mp4",
              "*_1080p*.mp4"]
b3 = '/var/log/wowza_delete_recordings.log'
logging.basicConfig(b4 = '%(asctime)s %(message)s', filename=b3, level=logging.INFO)
logging.info("Script started")
def fonk1(path, patterns):
    b5 = []
    for root, _, filenames in os.walk(path):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                b5.append(os.path.join(root, name))
    return b5
def fonk2(files):
    for file in files:
        os.remove(file)
        logging.info("Deleted file: %s", file)
def fonk3():
    b5 = fonk1(b1, b2)
    if not b5:
        logging.info("Nothing to delete")
    else:
        fonk2(b5)
    logging.info("Script ended")
if b6 = = "__main__":
    fonk3()