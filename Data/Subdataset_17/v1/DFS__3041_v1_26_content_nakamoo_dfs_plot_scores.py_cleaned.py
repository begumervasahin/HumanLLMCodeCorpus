import argparse
import matplotlib.pyplot as plt
import pandas as pd
def main():
    parser = argparse.ArgumentParser(description='Plot scores from a given file.')
    parser.add_argument('scores', type=str, help='Specify the path of scores.txt')
    parser.add_argument('--title', type=str, default=None, help='Title of the plot')
    args = parser.parse_args()
    scores = pd.read_csv(args.scores, delimiter='\t')
    for col in ['mean', 'median']:
        plt.plot(scores['steps'], scores[col], label=col)
    if args.title is not None:
        plt.title(args.title)
    plt.xlabel('Steps')
    plt.ylabel('Score')
    plt.legend(loc='best')
    fig_fname = args.scores + '.png'
    plt.savefig(fig_fname)
    print(f'Saved a figure as {fig_fname}')
if __name__ == '__main__':
    main()