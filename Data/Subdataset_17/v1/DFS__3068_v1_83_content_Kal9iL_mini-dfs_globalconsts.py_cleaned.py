from enum import Enum
operation_names = ("ls", "fetch", "upload", "read", "quit")
OPERATIONS = Enum("OPERATIONS", operation_names)
NameNode_path = "./dfs/NameNode"
DataNode_path = "./dfs/DataNode"
infofile = f"{NameNode_path}/info.pkl"
NUM_OF_DATASERVERS = 4
NUM_OF_REPLICAS = 3
CHUNK_SIZE = 2 * 1024 * 1024
def main():
    print("Operation Names:")
    for op in OPERATIONS:
        print(f"- {op.name}")
    print("\nConfiguration:")
    print(f"NameNode Path: {NameNode_path}")
    print(f"DataNode Path: {DataNode_path}")
    print(f"Info File Path: {infofile}")
    print(f"Number of Data Servers: {NUM_OF_DATASERVERS}")
    print(f"Number of Replicas: {NUM_OF_REPLICAS}")
    print(f"Chunk Size: {CHUNK_SIZE} bytes")
if __name__ == "__main__":
    main()