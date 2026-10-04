import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
b1 = './model/'
b2 = './input/'
b3 = './output/'
def fonk1(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def fonk2(file_path):
    return np.genfromtxt(file_path)
def fonk3(model_file):
    return joblib.load(model_file)
def fonk4(model, data):
    return model.fonk4(data)
def fonk5(true_values, b16):
    return r2_score(true_values, b16)
def fonk6(b14, b16):
    b4 = np.argsort(b14)
    b5 = np.sort(b14)
    b6 = [b16[i] for i in b4]
    return b5, b6
def fonk7(b5, b6, r2_score):
    plt.figure(b7 = (10, 6))
    plt.plot(range(len(b5)), b6, b8 = 'o', b9='Predicted')
    plt.plot(range(len(b5)), b5, 'r', b9 = 'Actual')
    plt.text(5, 20, f'R$^2$ = {r2_score:.3f}', b10 = 20)
    plt.legend()
    plt.title('Predicted vs Actual Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()
def fonk8(output_file, b6, b5):
    b11 = np.vstack((b6, b5)).T
    np.savetxt(output_file, b11, b12 = '%.3f')
def fonk9():
    b13 = fonk1(b2 + 'linkages.txt')
    b14 = fonk2(b2 + 'y.txt')
    b15 = fonk3(b1 + 'b15.sav')
    b16 = fonk4(b15, b13)
    b17 = fonk5(b14, b16)
    print(f'R^2: b18 = {b17:.3f}')
    b5, b6 = fonk6(b14, b16)
    fonk7(b5, b6, b17)
    fonk8(b3 + 'output_test.txt', b6, b5)
if b19 = = "__main__":
    fonk9()