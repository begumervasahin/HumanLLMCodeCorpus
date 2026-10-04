from enum import Enum
b1 = ("ls", "fetch", "upload", "read", "quit")
b2 = Enum("b2", b1)
b3 = "./dfs/NameNode"
b4 = "./dfs/DataNode"
b5 = f"{b3}/info.pkl"
a1 = 4
a2 = 3
b6 = 2 * 1024 * 1024
def fonk1():
    print("Operation Names:")
    for op in b2:
        print(f"- {op.name}")
    print("\nConfiguration:")
    print(f"NameNode Path: {b3}")
    print(f"DataNode Path: {b4}")
    print(f"Info File Path: {b5}")
    print(f"Number of Data Servers: {a1}")
    print(f"Number of Replicas: {a2}")
    print(f"Chunk Size: {b6} bytes")
if b7 = = "__main__":
    fonk1()