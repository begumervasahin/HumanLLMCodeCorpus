b1 = 'loaner'
from b3 import b3
from LDATopicSimilarity import TopicSimilarity
import sys
import cmd
class class1(cmd.Cmd):
    def fonk1(self, topic2vecSimilarity):
        cmd.Cmd.fonk1(self)
        self.b2 = topic2vecSimilarity
        self.b3 = self.b2.b3
        self.b4 = self.b2.model
        self.b5 = self.b3.ldaTopics
        self.b6 = self.b3.topicVecs
        print "Topic2vec Testing Suite"
        print "Commands are: "
        print "printTopic [b7] ~~ if no b7 is given, will print all"
        print "mostSimilar [b7]"
    def fonk2(self,b7 = None):
        if b7:
            print
            print b7
            print self.b5[int(b7)]
            print
        else:
            a1 = 0
            for topic in self.b5:
                print
                print a1
                print topic
                print
                a1+=1
    def fonk3(self, topic):
        b8 = []
        for y in range(0,50):
            b8.append(y)
        if int(topic) in b8:
            b9 = self.b2.findSimilarity(int(topic))
            print b9[0][0] + " | " + b9[1][0] + " | " + b9[2][0] + " | " + b9[3][0]
            print "----------------------------------"
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][0][1], b9[1][1][0][1], b9[2][1][0][1], b9[3][1][0][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][1][1], b9[1][1][1][1], b9[2][1][1][1], b9[3][1][1][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][2][1], b9[1][1][2][1], b9[2][1][2][1], b9[3][1][2][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][3][1], b9[1][1][3][1], b9[2][1][3][1], b9[3][1][3][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][4][1], b9[1][1][4][1], b9[2][1][4][1], b9[3][1][4][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][5][1], b9[1][1][5][1], b9[2][1][5][1], b9[3][1][5][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][6][1], b9[1][1][6][1], b9[2][1][6][1], b9[3][1][6][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][7][1], b9[1][1][7][1], b9[2][1][7][1], b9[3][1][7][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][8][1], b9[1][1][8][1], b9[2][1][8][1], b9[3][1][8][1])
            print "%d  |   %d  |  %d  | %d" % (b9[0][1][9][1], b9[1][1][9][1], b9[2][1][9][1], b9[3][1][9][1])
        else:
            print "Please Chose Acceptable Topic ID"
        print "Enter new command"