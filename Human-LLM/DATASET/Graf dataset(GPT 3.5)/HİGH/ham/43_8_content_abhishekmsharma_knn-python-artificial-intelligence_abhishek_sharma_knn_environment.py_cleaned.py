'''
Developer: Abhishek Manoj Sharma
Date: September 9, 2017
Class: class4
'''
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import class3
import os
'''
class4 class:
This class class1 two inputs from the main program - 1) directory name, 2) value of b5
It then iterates over the b2 present in the given directory, and passes the training set, b10, and b5 to the b1.
On receiving a prediction from the b1, the environment class class2 it with the expected output and calculates the b14.
Based on the b14 for different values of b5, it prints and output and plots a graph using the plotGraph() method of class class3.
'''
class class4:
    def fonk1(self,directory,b5):
        b1 = Agent()
        b2 = os.listdir(directory);
        b3 = []
        for file_names in b2:
            if file_names.endswith("tst.dat"):
                b3.append(file_names)
        b4 = len(b3)
        '''
        Calculating the number of iterations to be done for b17.
        For example:
        If b5 = 9, b14 will be calculated for 1,3,5,7,9.
        If b5 = 15, b14 will be calculated for 1,3,...,15.
        '''
        b6 = int(round(int(b5) / 2.0))
        print "| File Name", " " * (36 - len("File Name")),
        for i in range(1,int(b5)+1,2):
            print "| Accuracy (b5 = " + str(i) + ")" + " " * (17-len("Accuracy b17 = "+str(i))),
        print "|"
        b7 = [[0 for a2 in range (b6+1)] for a2 in range (b4)]
        for j in range(0, b4):
            b8 = directory + "
            b9 = b8.replace("tst.dat", "tra.dat")
            print "|",b3[j]," "*(36-len(b3[j])),"|",
            with open(b8) as test_file:
                for line in test_file:
                    '''
                    Data in the file starts from the line following the @data text
                    The if condition below checks for @data text in the file, and from there starts reading the data
                    '''
                    if "@data" in line:
                        for line in test_file:
                            b10 = line.strip().split(",")
                            b11 = b10[len(b10) - 1]
                            '''
                            The variable b12 stores the prediction received from the Agent
                            after sending b5, training file, and b10 to Agent'b16 sensor
                            '''
                            b12 = b1.sensor(b5, b9, b10)
                            a1 = 1
                            try:
                                b12 = map(float,b12)
                            except:
                                a1 = 0
                            a2 = 1
                            for item in b12:
                                if a1 = =0:
                                    if item.strip() == b11.strip():
                                        b7[j][a2] += 1
                                elif str(float(item)).strip() == str(float(b11)).strip():
                                        b7[j][a2] += 1
                                a2 += 1
                            b7[j][0] += 1
                b13 = b7[j]
            for n in range(1,len(b13)):
                b14 = str("{:.2f}".format(((float(b13[n])/b13[0])*100)))
                print b14+"% ("+str(b13[n]).zfill(3)+"/"+str(b13[0]).zfill(3)+")"+" " * (7-len(str(b14)))+"|",
            print ""
        b15 = []
        for outer_count in range(0,len(b7[0])):
            a3 = 0
            for inner_count in range(0,len(b7)):
                a3 = a3 + b7[inner_count][outer_count]
            b15.append(a3)
        print "-"* (42-len("-"))
        print "| Average Accuracies", " " * (36 - len("Average Accuracies")),"|"
        print "-" * (42 - len("-"))
        a4 = 1
        for items in range(1,len(b15)):
            b15[items]  = (float(b15[items])/b15[0]) * 100
            b16 = str("{:.2f}".format(b15[items]))
            print "b17 = "+str(a4)+": " + b16+"%"
            a4+=2
        b18 = class3()
        b18.plotGraph(b15[1:],directory)