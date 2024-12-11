import os
import logging
from myclass.class_compute_title_similarity import ComputeTitleSimilarity
from myclass.class_get_text_data_from_database import GetTextDataFromDB
def fonk1(filename, folder):
    return os.path.join(folder, filename)
def fonk2():
    b1 = "essayDB"
    b2 = GetTextDataFromDB(b1=b1)
    b3 = b2.count_essay_num(b1=b1)
    b4 = fonk1("stopword.txt", "./data/input")
    b5 = fonk1("word_map.txt", "./data/output")
    b6 = fonk1("title_id.txt", "./data/output")
    b7 = fonk1("cosine_similarity_result.txt", "./data/output")
    b8 = b2.get_title_list_in_db(b1=b1, b3=b3)
    logging.info(f"b8[1:4]: {b8[1:4]}")
    logging.info(f"b8[0]: {b8[0]}")
    logging.info(f"type(b8[0]): {type(b8[0])}")
    logging.info(f"len(b8): {len(b8)}")
    logging.info(f"type(b8): {type(b8)}")
    b9 = ComputeTitleSimilarity()
    b10 = b9.get_word_map_tuple_list(b8=b8, word_map_file_save_directory=b5)
    logging.info(f"b10[:10]: {b10[:10]}")
    b11 = b9.remove_stopword_in_title_list(b8=b8, stopword_file_read_directory=b4)
    b12 = b9.title_list_2_title_index_and_title_id_list_tuple_list(b8=b11, b10=b10, title_id_file_save_directory=b6)
    logging.info(f"b12[0:10]: {b12[0:10]}")
    logging.info(f"b12[0][0]: {b12[0][0]}")
    b13 = b9.title_index_and_title_id_list_tuple_list_2_word_key_value_pair_tuple_list(b12=b12)
    logging.info(f"b13[0]: {b13[0]}")
    logging.info(f"b13[0:5]: {b13[0:5]}")
    logging.info(f"b13[0][0]: {b13[0][0]}")
    b14 = b9.compute_title_similarity(id_title_tuple_2d_list=b13)
    logging.info(f"len(b14): {len(b14)}")
    logging.info(f"b14[0]: {b14[0]}")
    b15 = filter(lambda trigram_tuple: trigram_tuple[2] != 0, b14)
    b16 = sorted(b15, key=lambda trigram_tuple: -trigram_tuple[2])
    logging.info(f"b16[0]: {b16[0]}")
    logging.info(f"b16[1]: {b16[1]}")
    b9.save_compute_similarity_result(b16 = b16, cosine_similarity_result_file_save_directory=b7)
if b17 = = "__main__":
    fonk2()