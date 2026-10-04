
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class Environment:
    def send_to_agent(self, directory, k):
        agent = Agent()
        files = os.listdir(directory)
        testing_files = [file_name for file_name in files if file_name.endswith("tst.dat")]
        number_of_files = len(testing_files)
        number_of_iterations = int(round(int(k) / 2.0))
        header = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, int(k) + 1, 2):
            header += "| Accuracy (k=" + str(i) + ")" + " " * (17 - len("Accuracy (k=" + str(i) + ")"))
        print(header + "|")
        computed_stats = [[0 for _ in range(number_of_iterations + 1)] for _ in range(number_of_files)]
        for j, testing_file in enumerate(testing_files):
            testing_file_path = os.path.join(directory, testing_file)
            training_file_path = testing_file_path.replace("tst.dat", "tra.dat")
            print("|", testing_files[j], " " * (36 - len(testing_files[j])), "|", end='')
            with open(testing_file_path) as test_file:
                read_data = False
                for line in test_file:
                    if "@data" in line:
                        read_data = True
                        continue
                    if read_data:
                        percept = line.strip().split(",")
                        expected_prediction = percept[-1]
                        result = agent.sensor(k, training_file_path, percept)
                        alphabet_flag = 1
                        try:
                            result = list(map(float, result))
                        except ValueError:
                            alphabet_flag = 0
                        count = 1
                        for item in result:
                            if alphabet_flag == 0:
                                if item.strip() == expected_prediction.strip():
                                    computed_stats[j][count] += 1
                            elif str(float(item)).strip() == str(float(expected_prediction)).strip():
                                computed_stats[j][count] += 1
                            count += 1
                        computed_stats[j][0] += 1
            current_computed_value = computed_stats[j]
            for n in range(1, len(current_computed_value)):
                accuracy = (float(current_computed_value[n]) / current_computed_value[0]) * 100
                accuracy_str = f"{accuracy:.2f}% ({current_computed_value[n]:03}/{current_computed_value[0]:03})"
                print(accuracy_str + " " * (27 - len(accuracy_str)) + "|", end='')
            print("")
        all_stats = [sum(stats) for stats in zip(*computed_stats)]
        print("-" * 42)
        print("| Average Accuracies" + " " * (36 - len("Average Accuracies")) + "|")
        print("-" * 42)
        for i in range(1, len(all_stats)):
            average_accuracy = (float(all_stats[i]) / all_stats[0]) * 100
            print(f"K={i*2-1}: {average_accuracy:.2f}%")
        g = Graph()
        g.plotGraph(all_stats[1:], directory)