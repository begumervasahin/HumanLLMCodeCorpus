import numpy as np
import matplotlib.pyplot as plt
class class1:
    '''
    To modify display of the rendered results.
    '''
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
def fonk1(b22, b23):
    '''
    Calculate the Root Mean Squared Error for the model prediction.
    Parameters:
    b22 (numpy array): True values
    b23 (numpy array): Predicted values
    Returns:
    float: Root mean squared error
    '''
    b11 = b22.shape[0]
    b12 = b22 - b23
    b13 = np.sqrt(np.sum(b12**2) / b11)
    return b13
def fonk2(b22, b23):
    '''
    Calculate the R^2 Score for the model prediction.
    Parameters:
    b22 (numpy array): True values
    b23 (numpy array): Predicted values
    Returns:
    float: R^2 score
    '''
    b14 = np.sum((b22 - b23)**2)
    b15 = np.mean(b22)
    b16 = np.sum((b22 - b15)**2)
    b17 = 1 - (b14 / b16)
    return b17
def fonk3(b22, b23, a1, b24, b25):
    '''
    Display the performance information (R2 Score, RMSE, and b24 generated) for a candidate regression model.
    Parameters:
    b22 (numpy array): True values
    b23 (numpy array): Predicted values
    a1 (int): Degree of polynomial fitted
    b24 (list): Weights of the model
    b25 (str): Technique used to estimate the b24
    '''
    b18 = fonk2(b22, b23)
    b13 = fonk1(b22, b23)
    print(f"\n\n\n{class1.b8}{class1.b9}{b25}:{class1.b10}\n")
    print(f"R2-Score: {b18}")
    print(f"RMSE: {b13}")
    print(f"Weights Generated for Degree {a1}: {', '.join(str(weight) for weight in b24)}")
    print("\n\n\n")
def fonk4(b26, a2):
    '''
    Plot the halved mean square error b26 function used in gradient descent for every (a2) number of iterations.
    Parameters:
    b26 (list): Halved mean squared errors observed in each iteration of gradient descent
    a2 (int): Interval between successive plotting of b26 values
    '''
    plt.figure()
    b19 = np.arange(1, len(b26) + 1, a2)
    b20 = [b26[i - 1] for i in b19]
    plt.plot(b19, b20)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {a2} iterations)')
    plt.show()
if b21 = = "__main__":
    b22 = np.array([1, 2, 3, 4, 5])
    b23 = np.array([1.1, 1.9, 3.2, 4.1, 4.8])
    a1 = 2
    b24 = [0.5, 1.2, 0.3]
    b25 = "Batch Gradient Descent"
    fonk3(b22, b23, a1, b24, b25)
    b26 = [10, 8, 6, 4, 2, 1, 0.5]
    a2 = 1
    fonk4(b26, a2)