import argparse
import matplotlib.pyplot as plt
import pandas as pd
def parse_arguments():
    parser = argparse.ArgumentParser(description='Plot scores from a given file.')
    parser.add_argument('scores', type=str, help='Specify the path of scores.txt')
    parser.add_argument('--title', type=str, default=None, help='Title of the plot')
    return parser.parse_args()
def read_scores(file_path):
    return pd.read_csv(file_path, delimiter='\t')
def plot_scores(scores, title=None):
    for col in ['mean', 'median']:
        plt.plot(scores['steps'], scores[col], label=col)
    if title:
        plt.title(title)
    plt.xlabel('Steps')
    plt.ylabel('Score')
    plt.legend(loc='best')
def save_plot(file_path):
    fig_fname = f"{file_path}.png"
    plt.savefig(fig_fname)
    print(f'Saved a figure as {fig_fname}')
def main():
    args = parse_arguments()
    scores = read_scores(args.scores)
    plot_scores(scores, args.title)
    save_plot(args.scores)
if __name__ == '__main__':
    main()