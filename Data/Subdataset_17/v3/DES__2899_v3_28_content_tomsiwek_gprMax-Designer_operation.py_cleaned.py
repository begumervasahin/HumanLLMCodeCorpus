class TOperation:
    def __init__(self, o_type=None, shape=None, shape_num=None):
        self.o_type = o_type
        self.shape = shape
        self.shape_num = shape_num
    def set_operation(self, o_type=None, shape=None, shape_num=None):
        self.o_type = o_type
        self.shape = shape
        self.shape_num = shape_num
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