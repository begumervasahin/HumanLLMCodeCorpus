class TOperation(object):
    def __init__(self, o_type=None, **kwargs):
        self.set_operation(o_type, **kwargs)
    def set_operation(self, o_type=None, **kwargs):
        self.o_type = o_type
        self.shape = kwargs.pop('shape', None)
        self.num = kwargs.pop('num', None)
operation = TOperation(o_type="resize", shape="rectangle", num=1)
print("Operation Type:", operation.o_type)
print("Shape:", operation.shape)
print("Number:", operation.num)