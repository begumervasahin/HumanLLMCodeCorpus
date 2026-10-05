import os
import xattr
from datetime import datetime
def get_last_used_date(file_path):
    try:
        last_used_date = xattr.getxattr(file_path, 'com.apple.lastuseddate')
        last_used_date = datetime.fromtimestamp(int.from_bytes(last_used_date, byteorder='big'))
        return last_used_date
    except OSError:
        return None
if __name__ == "__main__":
    file_path = "/path/to/your/file"
    last_used_date = get_last_used_date(file_path)
    if last_used_date:
        print(f"Last used date of {file_path}: {last_used_date}")
    else:
        print(f"Unable to retrieve last used date for {file_path}")