import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
b1 = './b16/regression_model.sav'
b2 = './input/linkages.txt'
b3 = './input/y.txt'
b4 = './output/output_test.txt'
def fonk1(file_path):
    with open(file_path) as file:
        b5 = [list(map(float, line.split())) for line in file]
    return np.array(b5)
def fonk2(file_path):
    return np.genfromtxt(file_path)
def fonk3(model_path):
    return joblib.load(model_path)
def fonk4(b16, data):
    return b16.predict(data)
def fonk5(b15, b17):
    return r2_score(b15, b17)
def fonk6(b15, b17):
    b6 = np.argsort(b15)
    b7 = b15[b6]
    b8 = b17[b6]
    return b7, b8
def fonk7(b7, b8, b18):
    plt.figure(b9 = (10, 6))
    plt.plot(range(len(b7)), b8, b10 = 'o', b11='Predicted')
    plt.plot(range(len(b7)), b7, 'r', b11 = 'Actual')
    plt.text(5, 20, f'R$^2$ = {b18:.3f}', b12 = 20)
    plt.legend()
    plt.title('Predicted vs Actual Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()
def fonk8(output_path, b8, b7):
    b13 = np.column_stack((b8, b7))
    np.savetxt(output_path, b13, b14 = '%.3f')
def fonk9():
    b5 = fonk1(b2)
    b15 = fonk2(b3)
    b16 = fonk3(b1)
    b17 = fonk4(b16, b5)
    b18 = fonk5(b15, b17)
    print(f'R^2 Score: {b18:.3f}')
    b7, b8 = fonk6(b15, b17)
    fonk7(b7, b8, b18)
    fonk8(b4, b8, b7)
if b19 = = "__main__":
    fonk9()