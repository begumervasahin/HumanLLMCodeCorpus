from fs.memoryfs import MemoryFS
def create_directories(fs):
    directories = ['test', 'foo']
    for directory in directories:
        fs.makedir(directory)
def list_directory_contents(fs):
    for path, info in fs.walk.info(max_depth=1):
        entry_type = "[dir]" if info.is_dir else "[file]"
        print(f"{entry_type} {path}")
def main():
    fs = MemoryFS()
    create_directories(fs)
    list_directory_contents(fs)
if __name__ == "__main__":
    main()