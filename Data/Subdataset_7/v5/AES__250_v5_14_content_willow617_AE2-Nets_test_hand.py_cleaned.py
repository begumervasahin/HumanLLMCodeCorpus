import os
from utils.Dataset import Dataset
from model import model
from utils.print_result import print_result
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
def fonk1():
    b1 = Dataset('handwritten_2views')
    b3, b4, b2 = b1.load_data()
    b3 = b1.normalize(b3, axis=0)
    b4 = b1.normalize(b4, axis=0)
    b5 = len(set(b2))
    b6 = {
        'activation_functions': ['sigmoid'] * 4,
        'dimensions': [[240, 200], [216, 200], [64, 200], [64, 200]],
        'learning_rates': [1.0e-3, 1.0e-3, 1.0e-3, 1.0e-1],
        'b14': [10, 20, 50],
    }
    b7 = {
        'b10': 1,
        'b15': 100,
    }
    H, b8 = model(
        b3 = b3,
        b4 = b4,
        b9 = b2,
        b10 = b7['b10'],
        b11 = b6['dimensions'],
        b12 = b6['activation_functions'],
        b13 = b6['learning_rates'],
        b14 = b6['b14'],
        b15 = b7['b15']
    )
    print_result(b5, H, b8)
if b16 = = '__main__':
    fonk1()