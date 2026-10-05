import random
class FrenchLefffLemmatizer:
    def __init__(self, lefff_file_path=None, lefff_additional_file_path=None):
        self.LEFFF_FILE_STORAGE = lefff_file_path or "<path to>/lefff-3.4.mlex"
        self.LEFFF_ADDITIONAL_DATA_FILE_STORAGE = lefff_additional_file_path or "<path to>/lefff-3.4-addition.mlex"
        self.INFLECTED_FORM, self.POS, self.LEMMA, self.MISC, self.OLD_LEMMA = 0, 1, 2, 3, 4
        self.WORDNET_LEFFF_DIC = {'adj': 'a', 'adv': 'r', 'nc': 'n', 'np': 'n', 'v': 'v', 'auxAvoir': 'v', 'auxEtre': 'v'}
        self._initialize_lefff_table()
    def _initialize_lefff_table(self):
        set_pos_triplets = set()
        with open(self.LEFFF_FILE_STORAGE, encoding='utf-8') as lefff_file:
            for line in lefff_file:
                line = line[:-1]
                parts = line.split('\t')
                pos_triplet = (parts[self.INFLECTED_FORM], parts[self.POS], parts[self.LEMMA])
                if pos_triplet not in set_pos_triplets:
                    set_pos_triplets.add(pos_triplet)
        set_pos_triplets_to_remove, set_pos_triplets_to_add = set(), set()
        with open(self.LEFFF_ADDITIONAL_DATA_FILE_STORAGE, encoding='utf-8') as lefff_additional_data_file:
            for line_add in lefff_additional_data_file:
                line_add = line_add[:-1]
                parts = line_add.split('\t')
                new_pos_triplet = (parts[self.INFLECTED_FORM], parts[self.POS], parts[self.LEMMA])
                try:
                    old_pos_triplet = (parts[self.INFLECTED_FORM], parts[self.POS], parts[self.OLD_LEMMA])
                except IndexError as err:
                    print("Error! ", err)
                    print("Length", len(parts))
                    print(self.INFLECTED_FORM, self.OLD_LEMMA)
                    print(parts[self.INFLECTED_FORM])
                set_pos_triplets_to_remove.add(old_pos_triplet)
                set_pos_triplets_to_add.add(new_pos_triplet)
        set_pos_triplets_to_remove.add(('chiens', 'nc', 'chiens'))
        set_pos_triplets_to_add.add(('résidente', 'nc', 'résident'))
        set_pos_triplets_to_add.add(('résidentes', 'nc', 'résident'))
        set_pos_triplets_to_remove.add(('traductrice', 'nc', 'traductrice'))
        set_pos_triplets = (set_pos_triplets - set_pos_triplets_to_remove) | set_pos_triplets_to_add
        lefff_triplets_dict = {triplet[self.INFLECTED_FORM]: {triplet} for triplet in set_pos_triplets}
        self.LEFFF_TABLE = lefff_triplets_dict
    def is_wordnet_api(self, pos):
        return pos in ['a', 'n', 'r', 'v']
    def draw_random_sample(self, sample_size):
        leff_list = list(self.LEFFF_TABLE)
        return [self.LEFFF_TABLE[leff_list[i]] for i in random.sample(range(len(leff_list)), sample_size)]
    def show_leff_dict(self, end):
        for index, element in enumerate(self.LEFFF_TABLE):
            print(element)
            if index >= end:
                break
    def lemmatize(self, word, pos="n"):
        raw_word = word.lower() if not pos == "np" else word
        triplets_list = self.LEFFF_TABLE.get(raw_word, [])
        pos_couples_list = []
        if self.is_wordnet_api(pos):
            return next((triplet[self.LEMMA] for triplet in triplets_list
                         if triplet[self.POS] in self.WORDNET_LEFFF_DIC and
                         self.WORDNET_LEFFF_DIC[triplet[self.POS]] == pos), raw_word)
        for triplet in triplets_list:
            pos_couple = (triplet[self.LEMMA], triplet[self.POS])
            if pos_couple not in pos_couples_list:
                pos_couples_list.append(pos_couple)
        return pos_couples_list if pos_couples_list else (raw_word, 'np')
lemmatizer = FrenchLefffLemmatizer()
word_to_lemmatize = "chat"
pos_tag = "n"
result = lemmatizer.lemmatize(word_to_lemmatize, pos_tag)
print(f"Lemmatized result for '{word_to_lemmatize}' with POS '{pos_tag}': {result}")