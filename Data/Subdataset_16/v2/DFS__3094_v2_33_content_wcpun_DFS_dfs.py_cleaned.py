from b2.memoryfs import MemoryFS
def fonk1(b2):
    b2.makedir('test')
    b2.makedir('foo')
def fonk2(b2):
    for path, info in b2.walk.info(b1 = 1):
        if info.is_dir:
            print(f"[dir] {path}")
        else:
            print(f"[file] {path}")
def fonk3():
    b2 = MemoryFS()
    fonk1(b2)
    fonk2(b2)
if b3 = = "__main__":
    fonk3()