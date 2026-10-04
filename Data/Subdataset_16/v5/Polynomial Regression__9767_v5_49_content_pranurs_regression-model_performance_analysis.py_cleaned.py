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
    b12 = np.sqrt(np.mean((actual - predicted) ** 2))
    return b12
def fonk2(actual, predicted):
    b13 = np.mean(actual)
    b14 = np.sum((actual - b13) ** 2)
    b15 = np.sum((actual - predicted) ** 2)
    b16 = 1 - (b15 / b14)
    return b16
def fonk3(actual, predicted, degree, theta, training_technique):
    b17 = fonk2(actual, predicted)
    b12 = fonk1(actual, predicted)
    b18 = ', '.join(map(str, theta))
    print(f"\n\n\n{class1.b8}{class1.b9}{training_technique}:{class1.b10}\n")
    print(f"R2-Score: {b17}")
    print(f"RMSE: {b12}")
    print(f"Weights Generated for Degree {degree}: {b18}")
    print("\n\n\n")
def fonk4(cost, interval):
    b19 = np.arange(1, len(cost) + 1, interval)
    b20 = [cost[i - 1] for i in b19]
    plt.figure()
    plt.plot(b19, b20)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {interval} b19)')
    plt.show()