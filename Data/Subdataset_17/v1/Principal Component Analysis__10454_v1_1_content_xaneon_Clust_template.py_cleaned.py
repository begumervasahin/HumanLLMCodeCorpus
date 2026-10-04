import matplotlib.pyplot as plt
import numpy as np
def get(signal_chunks, showtemplate):
    n_signal_chunks = len(signal_chunks)
    signal_average = np.mean(signal_chunks, axis=0)
    std_quarter = np.mean(np.std(signal_chunks[0:int(len(signal_chunks) / 4)], axis=0), axis=0)
    test = signal_average.copy()
    test[0:(len(test)
    upper_limit = abs(test) + (5 * std_quarter)
    lower_limit = (np.mean(signal_average, axis=0) * np.ones(len(signal_average)) - (7 * std_quarter))
    new = []
    for k in range(len(upper_limit)):
        new.extend([upper_limit[k]] * 2)
    start_idx = int(len(new) / (4 / 1.5)) + int(4 * 1.5)
    upper_limit = new[start_idx:start_idx + len(upper_limit)]
    if showtemplate:
        plt.plot(signal_average)
        plt.plot(upper_limit, 'r--')
        plt.plot(lower_limit, 'r--')
        plt.show()
    intemp = []
    for i in range(n_signal_chunks):
        curr_trial = signal_chunks[i]
        gthan = (curr_trial > lower_limit)
        sthan = (curr_trial < upper_limit)
        total = np.logical_and(gthan, sthan)
        intemp.append(np.all(total))
    intemp = np.array(intemp)
    idcs = np.where(intemp)[0]
    print(f'{len(signal_chunks)} signals have been reduced to {len(idcs)}.\n')
    return idcs
