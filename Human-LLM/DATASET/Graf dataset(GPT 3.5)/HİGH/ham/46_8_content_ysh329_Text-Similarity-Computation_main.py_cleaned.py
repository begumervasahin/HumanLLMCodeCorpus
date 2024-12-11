b1 = 'yuens'
from myclass.class_compute_title_similarity import *
from myclass.class_get_text_data_from_database import *
def fonk1():
    b2 = "essayDB"
    b3 = GetTextDataFromDB(b2 = b2)
    b4 = b3.\
        count_essay_num(b2 = b2)
    b5 = "stopword.txt"
    b6 = "./data/input"
    b7 = os.path.join(b6,\
                                           b5)
    b8 = "word_map.txt"
    b9 = "./data/output"
    b10 = os.path.join(b9,\
                                                b8)
    b11 = "title_id.txt"
    b12 = "./data/output"
    b13 = os.path.join(b12,\
                                                b11)
    b14 = "cosine_similarity_result.txt"
    b15 = "./data/output"
    b16 = os.path.join(b15,\
                                                                b14)
    b4 = b3.\
        count_essay_num(b2 = b2)
    b17 = b3.get_title_list_in_db(b2 = b2,\
                                               b4 = b4)
    logging.info("b17[1:4]:%s" % str(b17[1:4]))
    logging.info("b17[0]:%s" % b17[0])
    logging.info("type(b17[0]):%s" % type(b17[0]))
    logging.info("len(b17):%s" % len(b17))
    logging.info("type(b17):%s" % type(b17))
    b18 = ComputeTitleSimilarity()
    logging.info("b4:%s" % b4)
    b19 = b18.\
        get_word_map_tuple_list(b17 = b17,\
                                b10 = b10)
    logging.info("b19[:10]: %s" % b19[:10])
    b20 = b18.\
        remove_stopword_in_title_list\
        (b17 = b17,\
         b7 = b7)
    b21 = b18.\
        title_list_2_title_index_and_title_id_list_tuple_list\
        (b17 = b20,\
         b19 = b19,\
         b13 = b13)
    logging.info("b21[0:10]:%s" % b21[0:10])
    logging.info("b21[0][0]:%s" % b21[0][0])
    b22 = b18.\
        title_index_and_title_id_list_tuple_list_2_word_key_value_pair_tuple_list\
        (b21 = b21)
    logging.info("b22[0]:%s" % str(b22[0]))
    logging.info("b22[0:5]:%s" % str(b22[0:5]))
    logging.info("b22[0][0]:%s" % str(b22[0][0]))
    b23 = b18.\
        compute_title_similarity\
        (b24 = b22)
    logging.info("len(b23):%s" % len(b23))
    logging.info("b23[0]:%s" % str(b23[0]))
    b25 = filter\
        (lambda trigram_tuple: trigram_tuple[2] != 0, b23)
    b26 = sorted(b25,
                                                  b27 = lambda trigram_tuple: -trigram_tuple[2])
    logging.info("b26[0]:%s" % str(b26[0]))
    logging.info("b26[1]:%s" % str(b26[1]))
    b18.save_compute_similarity_result\
        (b26 = b26,
         b16 = b16)
if b28 = = "__main__":
    fonk1()