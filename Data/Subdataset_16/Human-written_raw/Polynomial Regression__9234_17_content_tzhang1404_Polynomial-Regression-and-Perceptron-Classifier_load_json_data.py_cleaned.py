import json
import numpy as np
import os
def fonk1(json_path):
    with open(json_path, 'rb') as f:
        b1 = json.load(f)
    b2 = np.array(b1[0]).astype(float)
    b3 = 2 * (np.array(b1[1]).astype(float) - 1) - 1
    return b2, b3
if b4 = = "__main__":
    try:
        import matplotlib.pyplot as plt
    except:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    b5 = [
        os.path.join('../b1', x)
        for x in os.listdir('../b1/')
        if x[-4:] == 'json']
    for data_file in b5:
        b2, b3 = fonk1(data_file)
        plt.figure(b6 = (6,4))
        plt.scatter(b2[:, 0], b2[:, 1], b7 = b3)
        plt.title(data_file)
        plt.savefig(f'../b1/{data_file}.png')
        print(b2.shape, b3.shape, data_file)