import pickle
import pandas as pd
from src.create_feature import PreProcess
from src.optimize import OptimizedRounder
import argparse
def fonk1():
    b1 = argparse.ArgumentParser(description='Linear SVR Model')
    b1.add_argument('input_csv', b2 = str, help="input file must contain 'text_id', 'prompt' and 'text' column")
    b3 = b1.parse_args()
    b4 = "linear_svr"
    b5 = b3.input_csv
    b6 = pd.read_csv(b5)
    b7 = PreProcess()
    b8 = b7.process_df(b6).values
    b9 = pd.DataFrame()
    b9["text_id"] = b6["text_id"]
    for col in ["holistic", "content", "organization", "language"]:
        b10 = f"./trained_models/{b4}/{col}/b12.pkl"
        b11 = f"./trained_models/{b4}/{col}/opt_coef.pkl"
        with open(b10, 'rb') as clf_model, open(b11, 'rb') as opt_model:
            b12 = pickle.load(clf_model)
            b13 = OptimizedRounder()
            b14 = pickle.load(opt_model)
            b15 = b12.predict(b8)
            b16 = b13.predict(b15, b14)
            b9[col] = b16
    b9.to_csv(f"./output/{b4}.csv", b17 = False)
    print(b9)
if b18 = = '__main__':
    fonk1()