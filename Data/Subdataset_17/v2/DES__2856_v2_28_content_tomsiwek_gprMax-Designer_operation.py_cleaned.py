class TOperation:
    def __init__(self, o_type=None, **kwargs):
        self.set_operation(o_type, **kwargs)
    def set_operation(self, o_type=None, **kwargs):
        self.o_type = o_type
        self.shape = kwargs.get('shape', None)
        self.shape_num = kwargs.get('shape_num', None)
def main():
    class TShape:
        def __str__(self):
            return self.__class__.__name__
    class TRect(TShape):
        pass
    class TCylin(TShape):
        pass
    class TCylinSector(TShape):
        pass
    class TPolygon(TShape):
        pass
    shape_instance = TRect()
    operation = TOperation(o_type="create", shape=shape_instance, shape_num=1)
    print(f"Operation Type: {operation.o_type}")
    print(f"Shape: {operation.shape}")
    print(f"Shape Number: {operation.shape_num}")
if __name__ == "__main__":
    main()