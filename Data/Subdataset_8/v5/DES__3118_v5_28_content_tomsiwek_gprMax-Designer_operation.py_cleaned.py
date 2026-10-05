class TOperation:
    def __init__(self, operation_type=None, **kwargs):
        self.set_operation(operation_type, **kwargs)
    def set_operation(self, operation_type=None, **kwargs):
        self.operation_type = operation_type
        self.shape = kwargs.pop('shape', None)
        self.shape_index = kwargs.pop('shape_index', None)