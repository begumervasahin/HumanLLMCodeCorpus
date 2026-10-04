'''
Developer: Abhishek Manoj Sharma
Date: September 9, 2017
Class: Environment
'''
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
import os
'''
Environment class:
This class receives two inputs from the main program - 1) directory name, 2) value of k
It then iterates over the files present in the given directory, and passes the training set, percept, and k to the agent.
On receiving a prediction from the agent, the environment class compares it with the expected output and calculates the accuracy.
Based on the accuracy for different values of k, it prints and output and plots a graph using the plotGraph() method of class Graph.
'''
class Environment:
    def sendToAgent(self,directory,k):
        agent = Agent()
        files = os.listdir(directory);
        testing_files = []
        for file_names in files:
            if file_names.endswith("tst.dat"):
                testing_files.append(file_names)
        number_of_files = len(testing_files)
        '''
        Calculating the number of iterations to be done for K.
        For example:
        If k = 9, accuracy will be calculated for 1,3,5,7,9.
        If k = 15, accuracy will be calculated for 1,3,...,15.
        '''
        number_of_iterations=int(round(int(k) / 2.0))
        print "| File Name", " " * (36 - len("File Name")),
        for i in range(1,int(k)+1,2):
            print "| Accuracy (k=" + str(i) + ")" + " " * (17-len("Accuracy K = "+str(i))),
        print "|"
        computed_stats = [[0 for count in range (number_of_iterations+1)] for count in range (number_of_files)]
        for j in range(0, number_of_files):
            testing_file = directory + "
            training_file = testing_file.replace("tst.dat", "tra.dat")
            print "|",testing_files[j]," "*(36-len(testing_files[j])),"|",
            with open(testing_file) as test_file:
                for line in test_file:
                    '''
                    Data in the file starts from the line following the @data text
                    The if condition below checks for @data text in the file, and from there starts reading the data
                    '''
                    if "@data" in line:
                        for line in test_file:
                            percept = line.strip().split(",")
                            expected_prediction = percept[len(percept) - 1]
                            '''
                            The variable result stores the prediction received from the Agent
                            after sending k, training file, and percept to Agent's sensor
                            '''
                            result = agent.sensor(k, training_file, percept)
                            alphabet_flag=1
                            try:
                                result = map(float,result)
                            except:
                                alphabet_flag = 0
                            count = 1
                            for item in result:
                                if alphabet_flag==0:
                                    if item.strip() == expected_prediction.strip():
                                        computed_stats[j][count] += 1
                                elif str(float(item)).strip() == str(float(expected_prediction)).strip():
                                        computed_stats[j][count] += 1
                                count += 1
                            computed_stats[j][0] += 1
                current_computed_value = computed_stats[j]
            for n in range(1,len(current_computed_value)):
                accuracy = str("{:.2f}".format(((float(current_computed_value[n])/current_computed_value[0])*100)))
                print accuracy+"% ("+str(current_computed_value[n]).zfill(3)+"/"+str(current_computed_value[0]).zfill(3)+")"+" " * (7-len(str(accuracy)))+"|",
            print ""
        all_stats = []
        for outer_count in range(0,len(computed_stats[0])):
            total_count = 0
            for inner_count in range(0,len(computed_stats)):
                total_count  = total_count + computed_stats[inner_count][outer_count]
            all_stats.append(total_count)
        print "-"* (42-len("-"))
        print "| Average Accuracies", " " * (36 - len("Average Accuracies")),"|"
        print "-" * (42 - len("-"))
        counter = 1
        for items in range(1,len(all_stats)):
            all_stats[items]  = (float(all_stats[items])/all_stats[0]) * 100
            s = str("{:.2f}".format(all_stats[items]))
            print "K="+str(counter)+": " + s+"%"
            counter+=2
        g = Graph()
        g.plotGraph(all_stats[1:],directory)