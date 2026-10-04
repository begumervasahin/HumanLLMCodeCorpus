from enum import Enum
b1 = ("ls","fetch","upload","read","quit")
b2 = Enum("b2",b1)
b3 = "./dfs/NameNode"
b4 = "./dfs/DataNode"
b5 = b3 + "/info.pkl"
a1 = 4
a2 = 3
b6 = 2 * 1024 * 1024