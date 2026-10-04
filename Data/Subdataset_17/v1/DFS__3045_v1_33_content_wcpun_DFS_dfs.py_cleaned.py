from fs.memoryfs import MemoryFS
def create_directories(dfs):
    dfs.makedir('test')
    dfs.makedir('foo')
def list_directory_contents(dfs):
    for path, info in dfs.walk.info(max_depth=1):
        if info.is_dir:
            print("[dir] {}".format(path))
        else:
            print("[file] {}".format(path))
def main():
    dfs = MemoryFS()
    create_directories(dfs)
    list_directory_contents(dfs)
if __name__ == "__main__":
    main()