import os
import xattr
from datetime import datetime
def fonk1(b3):
    try:
        b1 = xattr.getxattr(b3, 'com.apple.lastuseddate')
        b1 = datetime.fromtimestamp(int.from_bytes(b1, byteorder='big'))
        return b1
    except OSError:
        return None
if b2 = = "__main__":
    b3 = "/path/to/your/file"
    b1 = fonk1(b3)
    if b1:
        print(f"Last used date of {b3}: {b1}")
    else:
        print(f"Unable to retrieve last used date for {b3}")