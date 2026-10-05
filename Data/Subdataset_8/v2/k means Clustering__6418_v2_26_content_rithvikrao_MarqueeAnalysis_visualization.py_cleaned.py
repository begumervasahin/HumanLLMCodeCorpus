import numpy as np
import matplotlib.pyplot as plt
def get_graph(ticker, start_time, end_time):
    financial_returns_scores = []
    growth_scores = []
    multiple_scores = []
    integrated_scores = []
    data = np.load('ticker_data_file.npy')
    company_name = ""
    for row in data:
        if row[1] == ticker:
            company_name = row[0]
            financial_returns_scores.append(row[5])
            growth_scores.append(row[6])
            multiple_scores.append(row[7])
            integrated_scores.append(row[8])
    plt.plot(financial_returns_scores, label='Financial Return Score')
    plt.plot(growth_scores, label='Growth Score')
    plt.plot(multiple_scores, label='Multiple Score')
    plt.plot(integrated_scores, label='Integrated Score')
    plt.title(f"Metrics for {company_name} from {start_time} to {end_time}")
    plt.legend()
    plt.ylabel("Score")
    plt.xlabel("Time")
    plt.savefig(f"{ticker}_data.png")
    plt.show()
get_graph('LULU', '2012-01-01', '2018-01-01')