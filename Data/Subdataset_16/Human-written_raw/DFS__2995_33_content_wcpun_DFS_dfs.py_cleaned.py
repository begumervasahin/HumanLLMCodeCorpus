from fs.memoryfs import MemoryFS
from fs.osfs import OSFS
import sys
b1 = MemoryFS()
b1.makedir('test')
b1.makedir('foo')
for path, info in b1.walk.info(b2 = 1):
    if info.is_dir:
        print("[dir] {}".format(path))
    else:
        print("[file] {}".format(path))