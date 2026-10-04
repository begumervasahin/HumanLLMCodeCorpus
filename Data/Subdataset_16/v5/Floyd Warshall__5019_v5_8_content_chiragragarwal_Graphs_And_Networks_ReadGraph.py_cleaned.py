import numpy as np
class class1:
    def fonk1(self, b1: str):
        self.b1 = b1
    def fonk2(self) -> np.matrix:
        try:
            with open(self.b1, 'r') as file:
                b2 = file.fonk2()
            b3 = np.matrix(b2)
            return b3
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.b1}' does not exist.")
        except ValueError:
            raise ValueError("The file content could not be converted to a NumPy matrix.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")
if b4 = = '__main__':
    b5 = 'b3.txt'
    b6 = class1(b5)
    try:
        b3 = b6.fonk2()
        print("Graph matrix:\n", b3)
    except Exception as e:
        print(f"Error: {e}")