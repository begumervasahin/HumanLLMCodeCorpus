import pickle
import pandas as pd
from src.create_feature import PreProcess
from src.optimize import OptimizedRounder
import argparse
def main():
    parser = argparse.ArgumentParser(description='Linear SVR Model')
    parser.add_argument('input_csv', type=str, help="Input file must contain 'text_id', 'prompt', and 'text' columns")
    args = parser.parse_args()
    model_name = "linear_svr"
    test_path = args.input_csv
    test_df = pd.read_csv(test_path)
    preprocessor = PreProcess()
    X = preprocessor.process_df(test_df).values
    result_df = pd.DataFrame()
    result_df["text_id"] = test_df["text_id"]
    for col in ["holistic", "content", "organization", "language"]:
        clf_path = f"./trained_models/{model_name}/{col}/clf.pkl"
        opt_path = f"./trained_models/{model_name}/{col}/opt_coef.pkl"
        with open(clf_path, 'rb') as clf_file, open(opt_path, 'rb') as opt_file:
            clf = pickle.load(clf_file)
            optimizer = OptimizedRounder()
            coef = pickle.load(opt_file)
            preds = clf.predict(X)
            int_preds = optimizer.predict(preds, coef)
            result_df[col] = int_preds
    result_df.to_csv(f"./output/{model_name}.csv", index=False)
    print(result_df)
if __name__ == '__main__':
    main()