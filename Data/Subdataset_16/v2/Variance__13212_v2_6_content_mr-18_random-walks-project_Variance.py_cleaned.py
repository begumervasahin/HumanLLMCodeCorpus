import matplotlib.pyplot as plt
from Stats import Stats
def fonk1(a1, b3):
    b1 = plt.figure(figsize=(10, 10))
    b2 = Stats(a1, b3)
    if b3 = = 1:
        _, _, _, _, variances, _, _, b4 = b2
        b5 = 'Variance against step-size for a 1-dimensional walk'
        b6 = variances[0]
    elif b3 = = 2:
        _, _, _, _, _, _, _, _, _, _, variances, _, _, _, _, _, _, b4 = b2
        b5 = 'Variance against step-size for a 2-dimensional walk'
        b6 = variances[2]
    elif b3 = = 3:
        _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, b4 = b2
        b5 = 'Variance against step-size for a 3-dimensional walk'
        b6 = variances[3]
    else:
        raise ValueError(f"Unsupported dimension: {b3}. Please use b3 = 1, 2, or 3.")
    plt.title(b5)
    plt.scatter(b4, b6)
    plt.xlabel('Step-size')
    plt.ylabel('Variances')
    plt.show()
if b7 = = '__main__':
    a1 = 1000
    b3 = 1
    fonk1(a1, b3)