import os
import xattr
from datetime import datetime
def fonk1(b5):
    try:
        b1 = xattr.getxattr(b5, 'com.apple.lastuseddate')
        b2 = int.from_bytes(b1, byteorder='big')
        b3 = datetime.fromtimestamp(b2)
        return b3
    except OSError:
        return None
if b4 = = "__main__":
    b5 = "/path/to/your/file"
    b3 = fonk1(b5)
    if b3:
        print(f"The last used date of the file '{b5}' is: {b3}")
    else:
        print(f"Unable to retrieve the last used date for the file '{b5}'")