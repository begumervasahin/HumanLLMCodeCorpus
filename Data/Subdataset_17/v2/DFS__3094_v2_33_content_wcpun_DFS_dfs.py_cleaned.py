from fs.memoryfs import MemoryFS
def create_directories(fs):
    fs.makedir('test')
    fs.makedir('foo')
def list_directory_contents(fs):
    for path, info in fs.walk.info(max_depth=1):
        if info.is_dir:
            print(f"[dir] {path}")
        else:
            print(f"[file] {path}")
def main():
    fs = MemoryFS()
    create_directories(fs)
    list_directory_contents(fs)
if __name__ == "__main__":
    main()