import pickle
import pandas as pd
from src.create_feature import PreProcess
from src.optimize import OptimizedRounder
import argparse
def main():
    parser = argparse.ArgumentParser(description='Linear SVR Model')
    parser.add_argument('input_csv', type=str, help="Path to the input CSV file containing 'text_id', 'prompt', and 'text' columns")
    args = parser.parse_args()
    model_name = "linear_svr"
    test_df = pd.read_csv(args.input_csv)
    preprocessor = PreProcess()
    X = preprocessor.process_df(test_df).values
    result_df = pd.DataFrame()
    result_df["text_id"] = test_df["text_id"]
    for col in ["holistic", "content", "organization", "language"]:
        clf_path = f"./trained_models/{model_name}/{col}/clf.pkl"
        opt_path = f"./trained_models/{model_name}/{col}/opt_coef.pkl"
        with open(clf_path, 'rb') as clf_model, open(opt_path, 'rb') as opt_model:
            clf = pickle.load(clf_model)
            optR = OptimizedRounder()
            coef = pickle.load(opt_model)
            preds = clf.predict(X)
            int_preds = optR.predict(preds, coef)
            result_df[col] = int_preds
    output_path = f"./output/{model_name}.csv"
    result_df.to_csv(output_path, index=False)
    print(f"Result saved to: {output_path}")
if __name__ == '__main__':
    main()