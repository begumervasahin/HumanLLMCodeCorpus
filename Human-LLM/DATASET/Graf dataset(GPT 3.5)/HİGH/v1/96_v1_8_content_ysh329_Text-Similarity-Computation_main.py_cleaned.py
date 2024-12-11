import os
import logging
from myclass.class_compute_title_similarity import ComputeTitleSimilarity
from myclass.class_get_text_data_from_database import GetTextDataFromDB
def fonk1():
    b1 = "essayDB"
    b2 = GetTextDataFromDB(b1=b1)
    b3 = b2.count_essay_num(b1=b1)
    b4 = "stopword.txt"
    b5 = "./data/input"
    b6 = os.path.join(b5, b4)
    b7 = "word_map.txt"
    b8 = "./data/output"
    b9 = os.path.join(b8, b7)
    b10 = "title_id.txt"
    b11 = "./data/output"
    b12 = os.path.join(b11, b10)
    b13 = "cosine_similarity_result.txt"
    b14 = "./data/output"
    b15 = os.path.join(b14, b13)
    b16 = b2.get_title_list_in_db(b1=b1, b3=b3)
    logging.info("b16[1:4]: %s" % str(b16[1:4]))
    logging.info("b16[0]: %s" % b16[0])
    logging.info("type(b16[0]): %s" % type(b16[0]))
    logging.info("len(b16): %s" % len(b16))
    logging.info("type(b16): %s" % type(b16))
    b17 = ComputeTitleSimilarity()
    logging.info("b3: %s" % b3)
    b18 = b17.get_word_map_tuple_list(b16=b16, b9=b9)
    logging.info("b18[:10]: %s" % b18[:10])
    b19 = b17.remove_stopword_in_title_list(b16=b16, b6=b6)
    b20 = b17.title_list_2_title_index_and_title_id_list_tuple_list(b16=b19, b18=b18, b12=b12)
    logging.info("b20[0:10]: %s" % b20[0:10])
    logging.info("b20[0][0]: %s" % b20[0][0])
    b21 = b17.title_index_and_title_id_list_tuple_list_2_word_key_value_pair_tuple_list(b20=b20)
    logging.info("b21[0]: %s" % str(b21[0]))
    logging.info("b21[0:5]: %s" % str(b21[0:5]))
    logging.info("b21[0][0]: %s" % str(b21[0][0]))
    b22 = b17.compute_title_similarity(id_title_tuple_2d_list=b21)
    logging.info("len(b22): %s" % len(b22))
    logging.info("b22[0]: %s" % str(b22[0]))
    b23 = filter(lambda trigram_tuple: trigram_tuple[2] != 0, b22)
    b24 = sorted(b23, key=lambda trigram_tuple: -trigram_tuple[2])
    logging.info("b24[0]: %s" % str(b24[0]))
    logging.info("b24[1]: %s" % str(b24[1]))
    b17.save_compute_similarity_result(b24 = b24, b15=b15)
if b25 = = "__main__":
    fonk1()