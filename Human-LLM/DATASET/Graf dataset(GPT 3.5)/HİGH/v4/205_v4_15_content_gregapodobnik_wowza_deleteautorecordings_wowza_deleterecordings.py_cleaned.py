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
    for pattern in b2:
        for name in fnmatch.filter(filenames, pattern):
            b6.append(os.path.join(root, name))
if not b6:
    logging.info("Nothing to delete")
else:
    for deleted_file in b6:
        os.remove(deleted_file)
        logging.info("Deleted file: %s", deleted_file)
logging.info("Script ended")