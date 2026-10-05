from topic2vec import topic2vec
from LDATopicSimilarity import TopicSimilarity
import sys
import cmd
class SimilaritySuite(cmd.Cmd):
    def __init__(self, topic2vec_similarity):
        cmd.Cmd.__init__(self)
        self.similarity = topic2vec_similarity
        self.topic2vec = self.similarity.topic2vec
        self.LDA_model = self.similarity.model
        self.topics = self.topic2vec.ldaTopics
        self.topic2vec_topics = self.topic2vec.topicVecs
        print("Topic2vec Testing Suite")
        print("Commands are:")
        print("printTopic [topicID] - If no topicID is given, will print all")
        print("mostSimilar [topicID]")
    def do_printTopic(self, topicID=None):
        if topicID:
            print("\n" + str(topicID))
            print(self.topics[int(topicID)])
            print()
        else:
            for i, topic in enumerate(self.topics):
                print("\n" + str(i))
                print(topic)
                print()
    def do_mostSimilar(self, topicID):
        acceptable = list(range(50))
        if int(topicID) in acceptable:
            output = self.similarity.findSimilarity(int(topicID))
            print(output[0][0] + " | " + output[1][0] + " | " + output[2][0] + " | " + output[3][0])
            print("----------------------------------")
            for i in range(10):
                print(" ".join(f"{output[j][1][i][1]:<6}" for j in range(4)))
        else:
            print("Please choose an acceptable Topic ID")
        print("Enter new command")
if __name__ == '__main__':
    topic2vecSimilarity = topic2vec()
    topicSimilarity = TopicSimilarity(topic2vecSimilarity)
    similarity_suite = SimilaritySuite(topicSimilarity)
    similarity_suite.cmdloop()