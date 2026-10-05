import numpy as np
import matplotlib.pyplot as plt
import mpld3
def fonk1(ticker, start_time, end_time):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = np.load('ticker_data_file.npy')
    b6 = ""
    for row in b5:
        if row[1] == ticker:
            b6 = row[0]
            b1.append(row[5])
            b2.append(row[6])
            b3.append(row[7])
            b4.append(row[8])
    plt.plot(b1, b7 = 'Financial Return Score')
    plt.plot(b2, b7 = 'Growth Score')
    plt.plot(b3, b7 = 'Multiple Score')
    plt.plot(b4, b7 = 'Integrated Score')
    plt.title("Metrics for " + b6 + " from " + start_time + " to " + end_time)
    plt.legend()
    plt.ylabel("Score")
    plt.xlabel("Time")
    plt.savefig(ticker + "_data.png")
fonk1('LULU', '2012-01-01', '2018-01-01')