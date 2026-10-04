from fs.memoryfs import MemoryFS
def create_directories(memory_fs):
    memory_fs.makedir('test')
    memory_fs.makedir('foo')
def list_directory_contents(memory_fs):
    for path, info in memory_fs.walk.info(max_depth=1):
        if info.is_dir:
            print(f"[dir] {path}")
        else:
            print(f"[file] {path}")
def main():
    memory_fs = MemoryFS()
    create_directories(memory_fs)
    list_directory_contents(memory_fs)
if __name__ == "__main__":
    main()