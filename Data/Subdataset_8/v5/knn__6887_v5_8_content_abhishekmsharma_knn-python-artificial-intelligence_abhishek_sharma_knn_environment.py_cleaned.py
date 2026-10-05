import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class Environment:
    def __init__(self):
        self.agent = Agent()
    def send_to_agent(self, directory, k):
        testing_files = [file for file in os.listdir(directory) if file.endswith("tst.dat")]
        num_files = len(testing_files)
        num_iterations = int(round(int(k) / 2.0))
        self.print_table_header(k)
        computed_stats = [[0] * (num_iterations + 1) for _ in range(num_files)]
        for idx, testing_file in enumerate(testing_files):
            training_file = testing_file.replace("tst.dat", "tra.dat")
            print("| {:<36}".format(testing_file), end="|")
            with open(os.path.join(directory, testing_file)) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            percept = line.strip().split(",")
                            expected_prediction = percept[-1]
                            result = self.agent.sensor(int(k), training_file, percept)
                            self.update_computed_stats(computed_stats[idx], result, expected_prediction)
                self.print_accuracy_results(computed_stats[idx])
        self.print_average_accuracies(computed_stats)
        self.plot_graph(computed_stats, directory)
    def update_computed_stats(self, stats, result, expected_prediction):
        result_float = [float(item) if isinstance(item, str) and item.strip().isdigit() else item for item in result]
        stats[0] += 1
        for idx, item in enumerate(result_float, start=1):
            if item == expected_prediction:
                stats[idx] += 1
    def print_table_header(self, k):
        print("| File Name                          ", end="")
        for i in range(1, int(k) + 1, 2):
            print("| Accuracy (k={})        ".format(i), end="")
        print("|")
    def print_accuracy_results(self, stats):
        for idx, count in enumerate(stats[1:], start=1):
            accuracy = (count / stats[0]) * 100 if stats[0] != 0 else 0
            print(" {:.2f}% ({} / {})      |".format(accuracy, count, stats[0]), end="")
        print()
    def print_average_accuracies(self, computed_stats):
        print("-" * 42)
        print("| Average Accuracies                 |")
        print("-" * 42)
        for idx, stats in enumerate(zip(*computed_stats)[1:], start=1):
            avg_accuracy = (sum(stats) / computed_stats[0][idx]) * 100 if computed_stats[0][idx] != 0 else 0
            print("| K={:<2}: {:.2f}%".format(idx * 2 - 1, avg_accuracy))
        print("-" * 42)
    def plot_graph(self, computed_stats, directory):
        g = Graph()
        accuracies = [sum(stats[1:]) / stats[0] * 100 if stats[0] != 0 else 0 for stats in computed_stats]
        g.plot_graph(accuracies, directory)