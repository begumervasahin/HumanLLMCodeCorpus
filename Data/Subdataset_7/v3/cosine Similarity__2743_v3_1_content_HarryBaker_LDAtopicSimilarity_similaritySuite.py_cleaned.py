from b2 import b2
from LDATopicSimilarity import TopicSimilarity
import cmd
class class1(cmd.Cmd):
    def fonk1(self, b11):
        super().fonk1()
        self.b1 = b11
        self.b2 = self.b1.b2
        self.b3 = self.b1.model
        self.b4 = self.b2.ldaTopics
        self.b5 = self.b2.topicVecs
        print("Topic2vec Testing Suite")
        print("Commands:")
        print("printTopic [topicID] - Print details of the specified topic")
        print("mostSimilar [topicID] - Print the most similar b4")
    def fonk2(self, b6 = None):
        if b6 is not None:
            print(f"\n{b6}")
            print(self.b4[int(b6)] + "\n")
        else:
            for i, topic in enumerate(self.b4):
                print(f"\n{i}")
                print(topic + "\n")
    def fonk3(self, b6):
        b7 = list(range(50))
        if int(b6) in b7:
            b8 = self.b1.find_similarity(int(b6))
            print("Topic  |  Similarity Scores")
            print("----------------------------")
            for i in range(10):
                print(" ".join(f"{b8[j][1][i][1]:<6}" for j in range(4)))
        else:
            print("Please choose a valid Topic ID")
        print("Enter a new command")
if b9 = = '__main__':
    b10 = b2()
    b11 = TopicSimilarity(b10)
    b12 = class1(b11)
    b12.cmdloop()