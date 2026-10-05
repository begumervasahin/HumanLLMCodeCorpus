import random
class FrenchLefffLemmatizer(object):
    def __init__(self, lefff_file_path=None, lefff_additional_file_path=None):
    def isWordnetAPI(self, pos):
        return pos in ['a', 'n', 'r', 'v']
    def drawRandomSample(self, sample_size):
        leff_list = list(self.LEFFF_TABLE)
        return [self.LEFFF_TABLE[leff_list[i]] for i in random.sample(range(len(leff_list)), sample_size)]
    def showLeffDict(self, end):
        index = 0
        for element in self.LEFFF_TABLE:
            index += 1
            print(element)
            if index > end:
                break
    def lemmatize(self, word, pos="n"):
        raw_word = word
        if not (pos == "np"):
            word = word.lower()
        if word in self.LEFFF_TABLE.keys():
            triplets_list = self.LEFFF_TABLE[word]
        else:
            triplets_list = []
        POS_couples_list = []
        if self.isWordnetAPI(pos):
            for triplet in triplets_list:
                if triplet[self.POS] in self.WORDNET_LEFFF_DIC.keys():
                    translated_POS_tag = self.WORDNET_LEFFF_DIC[triplet[self.POS]]
                    if translated_POS_tag == pos:
                        return triplet[self.LEMMA]
        else:
            for triplet in triplets_list:
                POS_couple = (triplet[self.LEMMA], triplet[self.POS])
                if POS_couple not in POS_couples_list:
                    POS_couples_list.append(POS_couple)
        if not POS_couples_list:
            if self.isWordnetAPI(pos):
                return raw_word
            elif raw_word[0].isupper():
                POS_couples_list = (raw_word, 'np')
        return POS_couples_list
lemmatizer = FrenchLefffLemmatizer()
word_to_lemmatize = "chat"
pos_tag = "n"
result = lemmatizer.lemmatize(word_to_lemmatize, pos_tag)
print(f"Lemmatized result for '{word_to_lemmatize}' with POS '{pos_tag}': {result}")