import matplotlib.pyplot as plt
from Stats import Stats
def fonk1(a1, b5):
    b1 = plt.figure(figsize=(10, 10))
    b2 = Stats(a1, b5)
    b3 = ''
    b4 = []
    if b5 = = 1:
        _, _, _, _, variances, _, _, b6 = b2
        b3 = 'Variance against step-size for a 1-dimensional walk'
        b4 = variances[0]
    elif b5 = = 2:
        _, _, _, _, _, _, _, _, _, _, variances, _, _, _, _, _, _, b6 = b2
        b3 = 'Variance against step-size for a 2-dimensional walk'
        b4 = variances[2]
    elif b5 = = 3:
        _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, b6 = b2
        b3 = 'Variance against step-size for a 3-dimensional walk'
        b4 = variances[3]
    else:
        raise ValueError(f"Unsupported dimension: {b5}. Please use b5 = 1, 2, or 3.")
    plt.title(b3)
    plt.scatter(b6, b4)
    plt.xlabel('Step-size')
    plt.ylabel('Variances')
    plt.show()
if b7 = = '__main__':
    a1 = 1000
    b5 = 1
    fonk1(a1, b5)