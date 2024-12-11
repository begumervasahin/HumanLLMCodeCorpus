import pickle
import pandas as pd
from src.create_feature import PreProcess
from src.optimize import OptimizedRounder
import argparse
b1 = argparse.ArgumentParser(description='Linear SVR Model')
b1.add_argument('input_csv', b2 = str, help="input file must contain 'text_id', 'prompt' and 'text' column")
b3 = b1.parse_args()
b4 = "linear_svr"
if b5 = = '__main__':
    b6 = b3.input_csv
    b7 = pd.read_csv(b6)
    b8 = PreProcess()
    b9 = b8.process_df(b7).values
    b10 = pd.DataFrame()
    b10["text_id"] = b7["text_id"]
    for col in ["holistic", "content", "organization", "language"]:
        b11 = f"./trained_models/{b4}/{col}/b13.pkl"
        b12 = f"./trained_models/{b4}/{col}/opt_coef.pkl"
        with open(b11, 'rb') as clf_model, open(b12, 'rb') as opt_model:
            b13 = pickle.load(clf_model)
            b14 = OptimizedRounder()
            b15 = pickle.load(opt_model)
            b16 = b13.predict(b9)
            b17 = b14.predict(b16, b15)
            b10[col] = b17
    b10.to_csv(f"./output/{b4}.csv", b18 = False)
    print(b10)