import sys
import json
import numpy as np
from utils import unequal_mean
import matplotlib.pyplot as plt
def fonk1(b10):
    b1 = json.load(open(b10+'/config.json'))
    b2 = [np.load(b10 + '/train_losses_'+str(b7)+'.npy') for b7 in range(b1['n_trials'])]
    b3 = [np.load(b10 + '/val_losses_'+str(b7)+'.npy') for b7 in range(b1['n_trials'])]
    b4 = np.mean([np.load(b10 + '/test_f1_'+str(b7)+'.npy') for b7 in range(b1['n_trials'])])
    print(b10, 'test f1:', b4)
    b5 = unequal_mean(b2)
    b6 = unequal_mean(b3)
    b7 = np.arange(len(b5))
    plt.plot(b7, b5, b8 = 'blue', label='train')
    plt.plot(b7, b6, b8 = 'red', label='val')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend()
    plt.savefig(b10+'/training_curve.png')
if b9 = = '__main__':
    assert len(sys.argv) == 2
    b10 = sys.argv[1]
    fonk1(b10)