import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename):
    return np.load(filename)
def fonk2(b7, ticker):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = ""
    for row in b7:
        if row[1] == ticker:
            b5 = row[0]
            b1.append(row[5])
            b2.append(row[6])
            b3.append(row[7])
            b4.append(row[8])
    return b5, b1, b2, b3, b4
def fonk3(ticker, start_time, end_time, b5, b1, b2, b3, b4):
    plt.plot(b1, b6 = 'Financial Return Score')
    plt.plot(b2, b6 = 'Growth Score')
    plt.plot(b3, b6 = 'Multiple Score')
    plt.plot(b4, b6 = 'Integrated Score')
    plt.title(f"Metrics for {b5} from {start_time} to {end_time}")
    plt.legend()
    plt.ylabel("Score")
    plt.xlabel("Time")
    plt.savefig(f"{ticker}_data.png")
    plt.show()
def fonk4(ticker, start_time, end_time):
    b7 = fonk1('ticker_data_file.npy')
    b5, b1, b2, b3, b4 = fonk2(b7, ticker)
    fonk3(ticker, start_time, end_time, b5, b1, b2, b3, b4)
fonk4('LULU', '2012-01-01', '2018-01-01')