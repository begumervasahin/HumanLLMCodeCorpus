from topic2vec import topic2vec
from LDATopicSimilarity import TopicSimilarity
import cmd
class SimilaritySuite(cmd.Cmd):
    def __init__(self, topic_similarity):
        super().__init__()
        self.similarity = topic_similarity
        self.topic2vec = self.similarity.topic2vec
        self.LDA_model = self.similarity.model
        self.topics = self.topic2vec.ldaTopics
        self.topic2vec_topics = self.topic2vec.topicVecs
        print("Topic2vec Testing Suite")
        print("Commands:")
        print("printTopic [topicID] - Print details of the specified topic")
        print("mostSimilar [topicID] - Print the most similar topics")
    def do_printTopic(self, topic_id=None):
        if topic_id is not None:
            print(f"\n{topic_id}")
            print(self.topics[int(topic_id)] + "\n")
        else:
            for i, topic in enumerate(self.topics):
                print(f"\n{i}")
                print(topic + "\n")
    def do_mostSimilar(self, topic_id):
        acceptable_ids = list(range(50))
        if int(topic_id) in acceptable_ids:
            output = self.similarity.find_similarity(int(topic_id))
            print("Topic  |  Similarity Scores")
            print("----------------------------")
            for i in range(10):
                print(" ".join(f"{output[j][1][i][1]:<6}" for j in range(4)))
        else:
            print("Please choose a valid Topic ID")
        print("Enter a new command")
if __name__ == '__main__':
    topic2vec_instance = topic2vec()
    topic_similarity = TopicSimilarity(topic2vec_instance)
    similarity_suite = SimilaritySuite(topic_similarity)
    similarity_suite.cmdloop()