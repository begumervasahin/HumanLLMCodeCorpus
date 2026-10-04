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
def fonk1(b21, b22):
    '''
    Calculate the Root Mean Squared Error for the model prediction.
    Arguments:
    b21 : numpy array of true values
    b22 : numpy array of b22 values
    Returns:
    float : root mean squared error
    '''
    b11 = b21.shape[0]
    b12 = b21 - b22
    b13 = np.sqrt(np.sum(b12**2) / b11)
    return b13
def fonk2(b21, b22):
    '''
    Calculate the R^2 Score for the model prediction.
    Arguments:
    b21 : numpy array of true values
    b22 : numpy array of b22 values
    Returns:
    float : R^2 score
    '''
    b14 = np.sum((b21 - b22)**2)
    b15 = np.mean(b21)
    b16 = np.sum((b21 - b15)**2)
    b17 = 1 - (b14 / b16)
    return b17
def fonk3(b21, b22, a1, b23, b24):
    '''
    Display the performance information (R2 Score, RMSE, and weights generated) for a candidate regression model.
    Arguments:
    b21 : numpy array of true values
    b22 : numpy array of b22 values
    a1 : int, the a1 of polynomial fitted
    b23 : list, the weights of the model
    b24 : str, the technique used to estimate the weights
    '''
    print(f"\n\n\n{class1.b8}{class1.b9}{b24}:{class1.b10}\n")
    print(f"R2-Score: {fonk2(b21, b22)}")
    print(f"RMSE: {fonk1(b21, b22)}")
    print(f"Weights Generated for Degree {a1}: {', '.join(str(weight) for weight in b23)}")
    print("\n\n\n")
def fonk4(b25, a2):
    '''
    Plot the halved mean square error b25 function used in gradient descent for every (a2) number of iterations.
    Arguments:
    b25 : list, containing the halved mean squared errors observed in each iteration of gradient descent
    a2 : int, specifies the a2 between successive plotting of b25 values
    '''
    plt.figure()
    b18 = np.arange(1, len(b25) + 1, a2)
    b19 = [b25[i - 1] for i in b18]
    plt.plot(b18, b19)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title(f'Plot of Cost vs Iterations (every {a2} iterations)')
    plt.show()
if b20 = = "__main__":
    b21 = np.array([1, 2, 3, 4, 5])
    b22 = np.array([1.1, 1.9, 3.2, 4.1, 4.8])
    a1 = 2
    b23 = [0.5, 1.2, 0.3]
    b24 = "Batch Gradient Descent"
    fonk3(b21, b22, a1, b23, b24)
    b25 = [10, 8, 6, 4, 2, 1, 0.5]
    a2 = 1
    fonk4(b25, a2)