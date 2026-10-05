import random
class FrenchLefffLemmatizer:
    def __init__(self, lefff_file_path=None, lefff_additional_file_path=None):
        self.LEFFF_FILE_STORAGE = lefff_file_path or "<path to>/lefff-3.4.mlex"
        self.LEFFF_ADDITIONAL_DATA_FILE_STORAGE = lefff_additional_file_path or "<path to>/lefff-3.4-addition.mlex"
        self.INFLECTED_FORM, self.POS, self.LEMMA, self.MISC, self.OLD_LEMMA = 0, 1, 2, 3, 4
        self.WORDNET_LEFFF_DIC = {'adj': 'a', 'adv': 'r', 'nc': 'n', 'np': 'n', 'v': 'v', 'auxAvoir': 'v', 'auxEtre': 'v'}
        self._initialize_lefff_table()
    def _initialize_lefff_table(self):
        set_POS_triplets = self._read_file(self.LEFFF_FILE_STORAGE)
        set_POS_triplets_to_add, set_POS_triplets_to_remove = self._process_additional_data()
        set_POS_triplets = (set_POS_triplets - set_POS_triplets_to_remove) | set_POS_triplets_to_add
        self.LEFFF_TABLE = self._create_lefff_table(set_POS_triplets)
    def _read_file(self, file_path):
        set_POS_triplets = set()
        with open(file_path, encoding='utf-8') as lefff_file:
            for line in lefff_file:
                line = line.rstrip('\n')
                line_parts = line.split('\t')
                POS_triplet = (line_parts[self.INFLECTED_FORM], line_parts[self.POS], line_parts[self.LEMMA])
                set_POS_triplets.add(POS_triplet)
        return set_POS_triplets
    def _process_additional_data(self):
        set_POS_triplets_to_remove = set()
        set_POS_triplets_to_add = set()
        with open(self.LEFFF_ADDITIONAL_DATA_FILE_STORAGE, encoding='utf-8') as lefff_additional_data_file:
            for line_add in lefff_additional_data_file:
                line_add = line_add.rstrip('\n')
                line_add_parts = line_add.split('\t')
                new_POS_triplet = (line_add_parts[self.INFLECTED_FORM], line_add_parts[self.POS],
                                   line_add_parts[self.LEMMA])
                try:
                    old_POS_triplet = (line_add_parts[self.INFLECTED_FORM], line_add_parts[self.POS],
                                       line_add_parts[self.OLD_LEMMA])
                except IndexError as err:
                    print("Error! ", err)
                    print("Length", len(line_add_parts))
                    print(self.INFLECTED_FORM, self.OLD_LEMMA)
                    print(line_add_parts[self.INFLECTED_FORM])
                set_POS_triplets_to_remove.add(old_POS_triplet)
                set_POS_triplets_to_add.add(new_POS_triplet)
        set_POS_triplets_to_remove.update({('chiens', 'nc', 'chiens'), ('traductrice', 'nc', 'traductrice')})
        set_POS_triplets_to_add.update({('résidente', 'nc', 'résident'), ('résidentes', 'nc', 'résident')})
        return set_POS_triplets_to_add, set_POS_triplets_to_remove
    def _create_lefff_table(self, set_POS_triplets):
        lefff_triplets_dict = {}
        for a_triplet in set_POS_triplets:
            lefff_triplets_dict.setdefault(a_triplet[self.INFLECTED_FORM], set()).add(a_triplet)
        return lefff_triplets_dict
    def is_wordnet_api(self, pos):
        return pos in ['a', 'n', 'r', 'v']
    def draw_random_sample(self, sample_size):
        leff_list = list(self.LEFFF_TABLE)
        return [self.LEFFF_TABLE[leff_list[i]] for i in random.sample(range(len(leff_list)), sample_size)]
    def show_leff_dict(self, end):
        index = 0
        for element in self.LEFFF_TABLE:
            index += 1
            print(element)
            if index > end:
                break
    def lemmatize(self, word, pos="n"):
        raw_word = word.lower() if not (pos == "np") else word
        if word in self.LEFFF_TABLE:
            triplets_list = self.LEFFF_TABLE[word]
        else:
            triplets_list = []
        if self.is_wordnet_api(pos):
            return self._lemmatize_wordnet_api(triplets_list, pos)
        return self._lemmatize_non_wordnet_api(triplets_list, raw_word, pos)
    def _lemmatize_wordnet_api(self, triplets_list, pos):
        for triplet in triplets_list:
            if triplet[self.POS] in self.WORDNET_LEFFF_DIC:
                translated_POS_tag = self.WORDNET_LEFFF_DIC[triplet[self.POS]]
                if translated_POS_tag == pos:
                    return triplet[self.LEMMA]
        return raw_word if self.is_wordnet_api(pos) else [(triplet[self.LEMMA], triplet[self.POS]) for triplet in triplets_list]
    def _lemmatize_non_wordnet_api(self, triplets_list, raw_word, pos):
        POS_couples_list = []
        for triplet in triplets_list:
            POS_couple = (triplet[self.LEMMA], triplet[self.POS])
            if POS_couple not in POS_couples_list:
                POS_couples_list.append(POS_couple)
        if not POS_couples_list:
            if raw_word[0].isupper():
                POS_couples_list = (raw_word, 'np')
        return POS_couples_list