import pandas as pd
import json
import argparse
def summarize_data(train_data, features, label):
    neg_x = train_data[train_data[label] == 0][features]
    pos_x = train_data[train_data[label] == 1][features]
    mean_neg_x = neg_x.mean(axis=0).to_dict()
    stdev_neg_x = neg_x.std(axis=0).to_dict()
    mean_pos_x = pos_x.mean(axis=0).to_dict()
    stdev_pos_x = pos_x.std(axis=0).to_dict()
    summary = {0: {}, 1: {}}
    for feat in features:
        summary[0][feat] = [mean_neg_x[feat], stdev_neg_x[feat]]
        summary[1][feat] = [mean_pos_x[feat], stdev_pos_x[feat]]
    return summary
def training(input_file, output_file, label):
    train_data = pd.read_csv(input_file)
    train_data.set_index('Date', inplace=True)
    features = train_data.select_dtypes(include='float64').columns.tolist()
    summary = summarize_data(train_data, features, label)
    with open(output_file, 'w') as out_file:
        json.dump(summary, out_file, indent=4)
def main():
    parser = argparse.ArgumentParser(description="Train a model by summarizing the training data.")
    parser.add_argument('-i', '--input_file', default='train-data.csv', dest='input_file',
                        help="Input file for training (default: train-data.csv)")
    parser.add_argument('-o', '--output_file', default='summary.json', dest='output_file',
                        help="Output summary file (default: summary.json)")
    parser.add_argument('-l', '--target_label', default='RainToday', dest='label',
                        help="Target label (default: RainToday)")
    args = parser.parse_args()
    training(args.input_file, args.output_file, args.label)
if __name__ == '__main__':
    main()