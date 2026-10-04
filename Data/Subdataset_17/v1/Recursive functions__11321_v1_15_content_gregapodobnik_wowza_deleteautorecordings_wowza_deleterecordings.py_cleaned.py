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
FILESTODELETE = []
for root, dirs, filenames in os.walk(PATH):
    for items in DELPATTERN:
        for name in fnmatch.filter(filenames, items):
            FILESTODELETE.append(os.path.join(root, name))
if not FILESTODELETE:
    logging.info("Nothing to delete")
else:
    for deleted in FILESTODELETE:
        os.remove(deleted)
        logging.info("Deleted file: %s", deleted)
logging.info("Script ended")