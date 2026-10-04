from enum import Enum
class Operations(Enum):
    LS = "ls"
    FETCH = "fetch"
    UPLOAD = "upload"
    READ = "read"
    QUIT = "quit"
NAME_NODE_PATH = "./dfs/NameNode"
DATA_NODE_PATH = "./dfs/DataNode"
INFO_FILE_PATH = f"{NAME_NODE_PATH}/info.pkl"
NUM_OF_DATA_SERVERS = 4
NUM_OF_REPLICAS = 3
CHUNK_SIZE = 2 * 1024 * 1024
def display_operations():
    print("Available Operations:")
    for operation in Operations:
        print(f"- {operation.value}")
def display_configuration():
    print("\nConfiguration Settings:")
    print(f"NameNode Path: {NAME_NODE_PATH}")
    print(f"DataNode Path: {DATA_NODE_PATH}")
    print(f"Info File Path: {INFO_FILE_PATH}")
    print(f"Number of Data Servers: {NUM_OF_DATA_SERVERS}")
    print(f"Number of Replicas: {NUM_OF_REPLICAS}")
    print(f"Chunk Size: {CHUNK_SIZE} bytes")
def main():
    display_operations()
    display_configuration()
if __name__ == "__main__":
    main()