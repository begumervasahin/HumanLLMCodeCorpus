import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class Environment:
    def sendToAgent(self, directory, k):
        agent = Agent()
        files = os.listdir(directory)
        testing_files = [file_name for file_name in files if file_name.endswith("tst.dat")]
        number_of_files = len(testing_files)
        number_of_iterations = int(round(int(k) / 2.0))
        print("| File Name", " " * (36 - len("File Name")), end="")
        for i in range(1, int(k) + 1, 2):
            print("| Accuracy (k=" + str(i) + ")" + " " * (17 - len("Accuracy K = " + str(i))), end="")
        print("|")
        computed_stats = [[0 for _ in range(number_of_iterations + 1)] for _ in range(number_of_files)]
        for j in range(number_of_files):
            testing_file = os.path.join(directory, testing_files[j])
            training_file = testing_file.replace("tst.dat", "tra.dat")
            print("|", testing_files[j], " " * (36 - len(testing_files[j])), "|", end="")
            with open(testing_file) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            percept = line.strip().split(",")
                            expected_prediction = percept[len(percept) - 1]
                            result = agent.sensor(k, training_file, percept)
                            alphabet_flag = 1
                            try:
                                result = map(float, result)
                            except:
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
                    accuracy = str("{:.2f}".format(((float(current_computed_value[n]) / current_computed_value[0]) * 100)))
                    print(accuracy + "% (" + str(current_computed_value[n]).zfill(3) + "/" + str(current_computed_value[0]).zfill(3) + ") " * (7 - len(str(accuracy))), "|", end="")
                print("")
        all_stats = []
        for outer_count in range(len(computed_stats[0])):
            total_count = 0
            for inner_count in range(len(computed_stats)):
                total_count += computed_stats[inner_count][outer_count]
            all_stats.append(total_count)
        print("-" * (42 - len("-")))
        print("| Average Accuracies", " " * (36 - len("Average Accuracies")), "|")
        print("-" * (42 - len("-")))
        counter = 1
        for items in range(1, len(all_stats)):
            all_stats[items] = (float(all_stats[items]) / all_stats[0]) * 100
            s = str("{:.2f}".format(all_stats[items]))
            print("K=" + str(counter) + ": " + s + "%")
            counter += 2
        g = Graph()
        g.plotGraph(all_stats[1:], directory)
if __name__ == "__main__":
    env = Environment()
    env.sendToAgent("directory_name", "value_of_k")