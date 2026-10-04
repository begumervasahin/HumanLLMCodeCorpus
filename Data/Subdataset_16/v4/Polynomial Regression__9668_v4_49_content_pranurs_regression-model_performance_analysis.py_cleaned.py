import numpy as np
import matplotlib.pyplot as plt
class class1:
    b1 = '\033[95m'
    b2 = '\033[96m'
    b3 = '\033[36m'
    b4 = '\033[94m'
    b5 = '\033[92m'
    b6 = '\033[93m'
    b7 = '\033[91m'
    b8 = '\033[1m'
    b9 = '\033[4m'
    b10 = '\033[0m'
def fonk1(actual, predicted):
    b11 = actual.shape[0]
    b12 = actual - predicted
    b13 = np.sqrt(np.sum(b12 ** 2) / b11)
    return b13
def fonk2(actual, predicted):
    b12 = actual - predicted
    b14 = np.sum(b12 ** 2)
    b15 = np.mean(actual)
    b16 = np.sum((actual - b15) ** 2)
    b17 = 1 - (b14 / b16)
    return b17
def fonk3(actual, predicted, degree, theta, training_technique):
    print(f"\n\n\n{class1.b8}{class1.b9}{training_technique}:{class1.b10}\n")
    print(f"R2-Score: {fonk2(actual, predicted)}")
    print(f"RMSE: {fonk1(actual, predicted)}")
    print(f"Weights Generated for Degree {degree}: {', '.join(map(str, theta))}")
    print("\n\n\n")
def fonk4(cost, interval):
    plt.figure()
    b18 = np.arange(1, len(cost) + 1, interval)
    b19 = [cost[i - 1] for i in b18]
    plt.plot(b18, b19)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {interval} iterations)')
    plt.show()