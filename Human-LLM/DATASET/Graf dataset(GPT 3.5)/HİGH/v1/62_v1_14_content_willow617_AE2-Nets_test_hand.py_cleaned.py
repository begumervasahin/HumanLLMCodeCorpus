import os
from utils.Dataset import Dataset
from model import model
from utils.print_result import print_result
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
if b1 = = '__main__':
    b2 = Dataset('handwritten_2views')
    b4, b5, b3 = b2.load_data()
    b4 = b2.normalize(b4, 0)
    b5 = b2.normalize(b5, 0)
    b6 = len(set(b3))
    act_ae1, act_ae2, act_dg1, b7 = 'sigmoid', 'sigmoid', 'sigmoid', 'sigmoid'
    b8 = [240, 200]
    b9 = [216, 200]
    b10 = [64, 200]
    b11 = [64, 200]
    a1 = 1
    a2 = 100
    a3 = 1.0e-3
    a4 = 1.0e-3
    a5 = 1.0e-3
    a6 = 1.0e-1
    a7 = 10
    a8 = 20
    b12 = [act_ae1, act_ae2, act_dg1, b7]
    b13 = [b8, b9, b10, b11]
    b14 = [a3, a4, a5, a6]
    a9 = 50
    b15 = [a7, a8, a9]
    H, b3 = model(b4, b5, b3, a1, b13, b12, b14, b15, a2)
    print_result(b6, H, b3)