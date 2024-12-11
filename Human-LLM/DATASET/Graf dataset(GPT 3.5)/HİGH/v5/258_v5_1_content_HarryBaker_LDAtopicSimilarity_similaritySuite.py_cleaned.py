from b2 import b2
from LDATopicSimilarity import TopicSimilarity
import sys
import cmd
class class1(cmd.Cmd):
    def fonk1(self, b10):
        cmd.Cmd.fonk1(self)
        self.b1 = b10
        self.b2 = self.b1.b2
        self.b3 = self.b1.model
        self.b4 = self.b2.ldaTopics
        self.b5 = self.b2.topicVecs
        print("Topic2vec Testing Suite")
        print("Commands are:")
        print("printTopic [b6] - If no b6 is given, will print all")
        print("mostSimilar [b6]")
    def fonk2(self, b6 = None):
        if b6:
            print(f"\n{b6}")
            print(self.b4[int(b6)])
            print()
        else:
            for i, topic in enumerate(self.b4):
                print(f"\n{i}")
                print(topic)
                print()
    def fonk3(self, b6):
        b7 = list(range(50))
        if int(b6) in b7:
            b8 = self.b1.findSimilarity(int(b6))
            print(b8[0][0], "|", b8[1][0], "|", b8[2][0], "|", b8[3][0])
            print("----------------------------------")
            for i in range(10):
                print(" ".join(f"{b8[j][1][i][1]:<6}" for j in range(4)))
        else:
            print("Please choose an b7 Topic ID")
        print("Enter new command")
if b9 = = '__main__':
    b10 = b2()
    b11 = TopicSimilarity(b10)
    b12 = class1(b11)
    b12.cmdloop()