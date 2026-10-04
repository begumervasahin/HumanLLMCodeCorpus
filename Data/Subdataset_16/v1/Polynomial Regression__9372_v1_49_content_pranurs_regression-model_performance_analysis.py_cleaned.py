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
def fonk1(actual, predicted):
    '''
    To calculate the Root Mean Squared Error for the model prediction.
    Arguments
    -----------
    actual : the truth values of target attribute altitude
    predicted : the predicted values for target variable altitude
    Returns
    ---------
    b13 : the root mean squared error
    '''
    b11 = actual.shape[0]
    b12 = actual - predicted
    b13 = np.sqrt(np.sum(b12**2) / b11)
    return b13
def fonk2(actual, predicted):
    '''
    To calculate the R^2 Score for the model prediction.
    More information can be found at https:
    Arguments
    -----------
    actual : the truth values of target attribute altitude
    predicted : the predicted values for target variable altitude
    Returns
    ---------
    b17 : the R squared score
    '''
    b12 = actual - predicted
    b14 = np.sum(b12**2)
    b15 = np.mean(actual)
    b16 = np.sum((actual - b15)**2)
    b17 = 1 - (b14 / b16)
    return b17
def fonk3(actual, predicted, degree, theta, trainingTechnique):
    '''
    To display the performance information (R2 Score, b13, and weights generated) for
    a candidate regression model.
    Arguments
    -----------
    actual : the truth values of target attribute altitude
    predicted : the predicted values for target variable altitude
    degree : the degree of polynomial fitted
    theta : the weights of the model for which performance is being analysed
    trainingTechnique : the technique (Batch Gradient Descent, Stochastic Gradient Descent, or Normal Equation Method)
                        used to estimate the weights of the model of interest.
    '''
    print("\n\n\n" + class1.b8 + class1.b9 + trainingTechnique + ":" + class1.b10 + "\n")
    print("R2-Score: ", fonk2(actual, predicted))
    print("b13: ", fonk1(actual, predicted))
    print("Weights Generated for Degree {}: {}".format(degree, ', '.join(str(weight) for weight in theta)))
    print("\n\n\n")
def fonk4(cost, interval):
    '''
    Plots the halved mean square error cost function used in gradient descent for every (interval) number
    of iterations of the algorithm, using the library matplotlib.pyplot.
    Arguments
    -----------
    cost : a Python list containing the halved mean squared errors as observed in each iteration of gradient descent.
    interval : specifies the interval between successive plotting of cost values
    '''
    plt.figure()
    b18 = np.arange(1, len(cost) + 1, interval)
    b19 = [cost[i - 1] for i in b18]
    plt.plot(b18, b19)
    plt.xlabel('Number of Iterations')
    plt.ylabel('Cost (Halved Mean Square Error)')
    plt.title('Plot of Cost vs Iterations (every {} iterations)'.format(interval))
    plt.show()