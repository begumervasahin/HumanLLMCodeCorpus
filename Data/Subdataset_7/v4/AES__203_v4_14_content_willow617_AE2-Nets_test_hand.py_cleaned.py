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
        'ae1': 'sigmoid',
        'ae2': 'sigmoid',
        'dg1': 'sigmoid',
        'dg2': 'sigmoid'
    }
    b7 = {
        'ae1': [240, 200],
        'ae2': [216, 200],
        'dg1': [64, 200],
        'dg2': [64, 200]
    }
    b8 = {
        'pretraining': 1.0e-3,
        'autoencoder': 1.0e-3,
        'discriminator': 1.0e-3,
        'hybrid': 1.0e-1
    }
    b9 = {
        'pretraining': 10,
        'total': 20,
        'hybrid': 50
    }
    a1 = 1
    a2 = 100
    H, b10 = model(b3=b3,
                           b4 = b4,
                           b11 = b2,
                           a1 = a1,
                           b12 = list(b7.values()),
                           b13 = list(b6.values()),
                           b14 = list(b8.values()),
                           b9 = list(b9.values()),
                           a2 = a2)
    print_result(b5, H, b10)
if b15 = = '__main__':
    fonk1()