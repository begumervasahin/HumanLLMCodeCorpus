import matplotlib.pyplot as plt
from Stats import Stats
def fonk1(a1, b3):
    b1 = plt.figure(figsize=(10, 10))
    b2 = Stats(a1, b3)
    if b3 = = 1:
        _, _, _, _, variances, _, _, b4 = b2
        plt.title('Variance against step-size for a 1-dimensional walk')
        plt.scatter(b4, variances[0])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    elif b3 = = 2:
        _, _, _, _, _, _, _, _, _, _, variances, _, _, _, _, _, _, b4 = b2
        plt.title('Variance against step-size for a 2-dimensional walk')
        plt.scatter(b4, variances[2])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    elif b3 = = 3:
        _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, b4 = b2
        plt.title('Variance against step-size for a 3-dimensional walk')
        plt.scatter(b4, variances[3])
        plt.xlabel('Step-size')
        plt.ylabel('Variances')
    else:
        raise ValueError("Unsupported dimension: {}. Please use b3 = 1, 2, or 3.".format(b3))
    plt.show()
if b5 = = '__main__':
    a1 = 1000
    b3 = 1
    fonk1(a1, b3)