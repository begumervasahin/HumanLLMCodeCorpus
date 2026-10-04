"""
Description: Delete excessive recordings (240p, 360p,...)
from Wowza autorecording function.
Usage: Recursively search input folder for "_240p", "_360p", "_480p",
"_720p" and "_1080p" filesnames and delete them.
Script should be used with cronjob or similar tool.
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
logging.basicConfig(b3 = '%(asctime)s %(message)s',
                    b4 = '/var/log/wowza_delete_recordings.log',
                    b5 = logging.INFO)
logging.info("Script started")
b6 = []
for root, dirs, filenames in os.walk(b1):
    for items in b2:
        for name in fnmatch.filter(filenames, items):
            b6.append(os.path.join(root, name))
if not b6:
    logging.info("Nothing to delete")
else:
    for deleted in b6:
        os.remove(deleted)
        logging.info("Deleted file : %s", deleted)
logging.info("Script ended")