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
FILES_TO_DELETE = []
for root, dirs, filenames in os.walk(PATH):
    for pattern in DELPATTERN:
        for name in fnmatch.filter(filenames, pattern):
            FILES_TO_DELETE.append(os.path.join(root, name))
if not FILES_TO_DELETE:
    logging.info("Nothing to delete")
else:
    for deleted_file in FILES_TO_DELETE:
        os.remove(deleted_file)
        logging.info("Deleted file: %s", deleted_file)
logging.info("Script ended")