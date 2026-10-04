from enum import Enum
class class1(Enum):
    b1 = "ls"
    b2 = "fetch"
    b3 = "upload"
    b4 = "read"
    b5 = "quit"
b6 = "./dfs/NameNode"
b7 = "./dfs/DataNode"
b8 = f"{b6}/info.pkl"
a1 = 4
a2 = 3
b9 = 2 * 1024 * 1024
def fonk1():
    print("Available class1:")
    for operation in class1:
        print(f"- {operation.value}")
    print("\nConfiguration Settings:")
    print(f"NameNode Path: {b6}")
    print(f"DataNode Path: {b7}")
    print(f"Info File Path: {b8}")
    print(f"Number of Data Servers: {a1}")
    print(f"Number of Replicas: {a2}")
    print(f"Chunk Size: {b9} bytes")
if b10 = = "__main__":
    fonk1()