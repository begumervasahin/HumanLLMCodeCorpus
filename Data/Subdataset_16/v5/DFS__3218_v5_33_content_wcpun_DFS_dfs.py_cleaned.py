from b4.memoryfs import MemoryFS
def fonk1(b4):
    b1 = ['test', 'foo']
    for directory in b1:
        b4.makedir(directory)
def fonk2(b4):
    for path, info in b4.walk.info(b2 = 1):
        b3 = "[dir]" if info.is_dir else "[file]"
        print(f"{b3} {path}")
def fonk3():
    b4 = MemoryFS()
    fonk1(b4)
    fonk2(b4)
if b5 = = "__main__":
    fonk3()