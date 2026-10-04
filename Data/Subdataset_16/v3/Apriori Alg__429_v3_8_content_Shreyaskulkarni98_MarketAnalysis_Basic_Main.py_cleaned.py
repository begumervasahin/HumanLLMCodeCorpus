import pandas as pd
from apyori import apriori
def fonk1(b11):
    return pd.read_csv(b11, b1 = None)
def fonk2(data):
    b2 = []
    for i in range(len(data)):
        b3 = [str(data.values[i, j]) for j in range(data.shape[1]) if str(data.values[i, j]) != 'nan']
        b2.append(b3)
    return b2
def fonk3(b2, b4, b5, min_lift, b6):
    return list(apriori(b2, b4 = b4,
                        b5 = b5, min_lift=min_lift,
                        b6 = b6))
def fonk4(rules):
    print(f"Number of association rules: {len(rules)}")
    for rule in rules:
        b7 = list(rule.b7)
        b8 = rule.b8
        b9 = rule.ordered_statistics[0].b9
        b10 = rule.ordered_statistics[0].b10
        print(f"Rule: {b7[0]} -> {b7[1]}")
        print(f"Support: {b8}")
        print(f"Confidence: {b9}")
        print(f"Lift: {b10}")
        print("=====================================")
def fonk5():
    b11 = 'D:/Shreyas Kulkarni/Documents/PycharmProjects/MarketAnalysis_Apriori_Basic/b12.csv'
    b12 = fonk1(b11)
    print(b12.head())
    b2 = fonk2(b12)
    b13 = fonk3(b2, b4=0.0045, b5=0.2, min_lift=3, b6=2)
    fonk4(b13)
if b14 = = "__main__":
    fonk5()