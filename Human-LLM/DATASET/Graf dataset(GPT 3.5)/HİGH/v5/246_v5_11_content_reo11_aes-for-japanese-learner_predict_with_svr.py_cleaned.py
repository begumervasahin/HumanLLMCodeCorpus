import pickle
import pandas as pd
from src.create_feature import PreProcess
from src.optimize import OptimizedRounder
import argparse
def fonk1():
    b1 = argparse.ArgumentParser(description='Linear SVR Model')
    b1.add_argument('input_csv', b2 = str, help="Path to the input CSV file containing 'text_id', 'prompt', and 'text' columns")
    b3 = b1.parse_args()
    b4 = "linear_svr"
    b5 = pd.read_csv(b3.input_csv)
    b6 = PreProcess()
    b7 = b6.process_df(b5).values
    b8 = pd.DataFrame()
    b8["text_id"] = b5["text_id"]
    for col in ["holistic", "content", "organization", "language"]:
        b9 = f"./trained_models/{b4}/{col}/b11.pkl"
        b10 = f"./trained_models/{b4}/{col}/opt_coef.pkl"
        with open(b9, 'rb') as clf_model, open(b10, 'rb') as opt_model:
            b11 = pickle.load(clf_model)
            b12 = OptimizedRounder()
            b13 = pickle.load(opt_model)
            b14 = b11.predict(b7)
            b15 = b12.predict(b14, b13)
            b8[col] = b15
    b16 = f"./output/{b4}.csv"
    b8.to_csv(b16, b17 = False)
    print(f"Result saved to: {b16}")
if b18 = = '__main__':
    fonk1()