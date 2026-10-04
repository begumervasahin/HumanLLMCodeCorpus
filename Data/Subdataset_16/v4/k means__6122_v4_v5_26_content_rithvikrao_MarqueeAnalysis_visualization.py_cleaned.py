import numpy as np
import matplotlib.pyplot as plt
def fonk1(file_path):
    return np.load(file_path)
def fonk2(b8, ticker):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = ""
    for row in b8:
        if row[1] == ticker:
            b5 = row[0]
            b1.append(row[5])
            b2.append(row[6])
            b3.append(row[7])
            b4.append(row[8])
    return b5, b1, b2, b3, b4
def fonk3(b5, start_time, end_time, ticker, b1, b2, b3, b4):
    plt.figure(b6 = (10, 6))
    plt.plot(b1, b7 = 'Financial Return Score')
    plt.plot(b2, b7 = 'Growth Score')
    plt.plot(b3, b7 = 'Multiple Score')
    plt.plot(b4, b7 = 'Integrated Score')
    plt.title(f"Metrics for {b5} from {start_time} to {end_time}")
    plt.legend()
    plt.ylabel("Score")
    plt.xlabel("Time")
    plt.grid(True)
    plt.savefig(f"{ticker}_data.png")
    plt.close()
def fonk4(ticker, start_time, end_time):
    b8 = fonk1('ticker_data_file.npy')
    b5, b1, b2, b3, b4 = fonk2(b8, ticker)
    fonk3(b5, start_time, end_time, ticker, b1, b2, b3, b4)
fonk4('LULU', '2012-01-01', '2018-01-01')