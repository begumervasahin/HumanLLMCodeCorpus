import os
import xattr
from datetime import datetime
def get_last_used_date(file_path):
    try:
        last_used_date_bytes = xattr.getxattr(file_path, 'com.apple.lastuseddate')
        last_used_timestamp = int.from_bytes(last_used_date_bytes, byteorder='big')
        last_used_date = datetime.fromtimestamp(last_used_timestamp)
        return last_used_date
    except OSError:
        return None
if __name__ == "__main__":
    file_path = "/path/to/your/file"
    last_used_date = get_last_used_date(file_path)
    if last_used_date:
        print(f"The last used date of the file '{file_path}' is: {last_used_date}")
    else:
        print(f"Unable to retrieve the last used date for the file '{file_path}'")