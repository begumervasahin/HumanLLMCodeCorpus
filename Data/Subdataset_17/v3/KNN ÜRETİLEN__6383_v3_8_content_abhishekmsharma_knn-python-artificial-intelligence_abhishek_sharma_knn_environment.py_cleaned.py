
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class Environment:
    def send_to_agent(self, directory, k):
        agent = Agent()
        files = os.listdir(directory)
        testing_files = [file for file in files if file.endswith("tst.dat")]
        number_of_files = len(testing_files)
        number_of_iterations = int((k + 1) / 2)
        header = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, k + 1, 2):
            header += f"| Accuracy (k={i})" + " " * (17 - len(f"Accuracy (k={i})"))
        print(header + "|")
        computed_stats = [[0] * (number_of_iterations + 1) for _ in range(number_of_files)]
        for j, testing_file in enumerate(testing_files):
            testing_file_path = os.path.join(directory, testing_file)
            training_file_path = testing_file_path.replace("tst.dat", "tra.dat")
            row = f"| {testing_file}{' ' * (36 - len(testing_file))} |"
            with open(testing_file_path) as test_file:
                data_started = False
                for line in test_file:
                    if "@data" in line:
                        data_started = True
                        continue
                    if data_started:
                        percept = line.strip().split(",")
                        expected_prediction = percept[-1]
                        result = agent.sensor(k, training_file_path, percept)
                        alphabet_flag = not all(item.isdigit() for item in result)
                        for count, item in enumerate(result, start=1):
                            if alphabet_flag:
                                if item.strip() == expected_prediction.strip():
                                    computed_stats[j][count] += 1
                            else:
                                if str(float(item)).strip() == str(float(expected_prediction)).strip():
                                    computed_stats[j][count] += 1
                            computed_stats[j][0] += 1
            current_computed_value = computed_stats[j]
            for n in range(1, len(current_computed_value)):
                accuracy = "{:.2f}".format((current_computed_value[n] / current_computed_value[0]) * 100)
                row += f"{accuracy}% ({str(current_computed_value[n]).zfill(3)}/{str(current_computed_value[0]).zfill(3)}){' ' * (7 - len(accuracy))}|"
            print(row)
        all_stats = [sum(column) for column in zip(*computed_stats)]
        print("-" * 42)
        print(f"| {'Average Accuracies':<36} |")
        print("-" * 42)
        for counter in range(1, len(all_stats), 2):
            all_stats[counter] = (all_stats[counter] / all_stats[0]) * 100
            accuracy = "{:.2f}".format(all_stats[counter])
            print(f"K={counter}: {accuracy}%")
        graph = Graph()
        graph.plotGraph(all_stats[1:], directory)
if __name__ == '__main__':
    directory = input("Enter the directory name: ")
    k = int(input("Enter the value of k: "))
    env = Environment()
    env.send_to_agent(directory, k)