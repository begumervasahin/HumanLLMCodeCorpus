import os
import fnmatch
import logging
def fonk1(directory, patterns):
    b1 = []
    for root, _, filenames in os.walk(directory):
        for pattern in patterns:
            for name in fnmatch.filter(filenames, pattern):
                b2 = os.path.join(root, name)
                os.remove(b2)
                b1.append(b2)
    return b1
def fonk2(b8):
    logging.basicConfig(b3 = '%(asctime)s %(message)s',
                        b4 = b8,
                        b5 = logging.INFO)
def fonk3():
    b6 = "/path/to/wowza/recording/dir"
    b7 = ["*_240p*.mp4",
                         "*_360p*.mp4",
                         "*_480p*.mp4",
                         "*_720p*.mp4",
                         "*_1080p*.mp4"]
    b8 = '/var/log/wowza_delete_recordings.log'
    fonk2(b8)
    logging.info("Script started")
    b1 = fonk1(b6, b7)
    if not b1:
        logging.info("Nothing to delete")
    else:
        for deleted_file in b1:
            logging.info("Deleted file: %s", deleted_file)
    logging.info("Script ended")
if b9 = = "__main__":
    fonk3()