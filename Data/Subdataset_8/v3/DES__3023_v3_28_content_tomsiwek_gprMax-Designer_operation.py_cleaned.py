class TOperation:
    def __init__(self, operation_type=None, shape=None, index=None):
        self.operation_type = operation_type
        self.shape = shape
        self.index = index
operation = TOperation(operation_type="resize", shape="rectangle", index=1)
print("Operation Type:", operation.operation_type)
print("Shape:", operation.shape)
print("Index:", operation.index)