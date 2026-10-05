class TOperation:
    def __init__(self, operation_type=None, **kwargs):
        self.set_operation(operation_type, **kwargs)
    def set_operation(self, operation_type=None, **kwargs):
        self.o_type = operation_type
        self.shape = kwargs.pop('shape', None)
        self.shape_num = kwargs.pop('shape_num', None)