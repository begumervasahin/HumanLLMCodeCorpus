import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename):
    return np.load(filename)
def fonk2(b8, ticker):
    b1 = ""
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    for row in b8:
        if row[1] == ticker:
            b1 = row[0]
            b2.append(row[5])
            b3.append(row[6])
            b4.append(row[7])
            b5.append(row[8])
    return b1, b2, b3, b4, b5
def fonk3(ticker, start_time, end_time, b1, b2, b3, b4, b5):
    plt.figure(b6 = (10, 6))
    plt.plot(b2, b7 = 'Financial Return Score')
    plt.plot(b3, b7 = 'Growth Score')
    plt.plot(b4, b7 = 'Multiple Score')
    plt.plot(b5, b7 = 'Integrated Score')
    plt.title(f"Metrics for {b1} from {start_time} to {end_time}")
    plt.legend()
    plt.ylabel("Score")
    plt.xlabel("Time")
    plt.savefig(f"{ticker}_data.png")
    plt.show()
def fonk4(ticker, start_time, end_time):
    b8 = fonk1('ticker_data_file.npy')
    b1, b2, b3, b4, b5 = fonk2(b8, ticker)
    fonk3(ticker, start_time, end_time, b1, b2, b3, b4, b5)
if b9 = = "__main__":
    fonk4('LULU', '2012-01-01', '2018-01-01')