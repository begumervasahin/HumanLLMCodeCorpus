class TOperation:
    def __init__(self, o_type=None, shape=None, num=None):
        self.o_type = o_type
        self.shape = shape
        self.num = num
operation = TOperation(o_type="resize", shape="rectangle", num=1)
print("Operation Type:", operation.o_type)
print("Shape:", operation.shape)
print("Number:", operation.num)