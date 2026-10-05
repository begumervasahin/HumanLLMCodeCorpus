import os
import logging
from myclass.class_compute_title_similarity import ComputeTitleSimilarity
from myclass.class_get_text_data_from_database import GetTextDataFromDB
def setup_file_paths(filename, folder):
    return os.path.join(folder, filename)
def main():
    database_name = "essayDB"
    text_data_manager = GetTextDataFromDB(database_name=database_name)
    table_name_list = text_data_manager.count_essay_num(database_name=database_name)
    stopword_file = setup_file_paths("stopword.txt", "./data/input")
    word_map_file = setup_file_paths("word_map.txt", "./data/output")
    title_id_file = setup_file_paths("title_id.txt", "./data/output")
    cosine_similarity_result_file = setup_file_paths("cosine_similarity_result.txt", "./data/output")
    title_list = text_data_manager.get_title_list_in_db(database_name=database_name, table_name_list=table_name_list)
    logging.info(f"title_list[1:4]: {title_list[1:4]}")
    logging.info(f"title_list[0]: {title_list[0]}")
    logging.info(f"type(title_list[0]): {type(title_list[0])}")
    logging.info(f"len(title_list): {len(title_list)}")
    logging.info(f"type(title_list): {type(title_list)}")
    cosine_computer = ComputeTitleSimilarity()
    word_map_tuple_list = cosine_computer.get_word_map_tuple_list(title_list=title_list, word_map_file_save_directory=word_map_file)
    logging.info(f"word_map_tuple_list[:10]: {word_map_tuple_list[:10]}")
    stopword_removed_title_list = cosine_computer.remove_stopword_in_title_list(title_list=title_list, stopword_file_read_directory=stopword_file)
    title_index_and_title_id_list_tuple_list = cosine_computer.title_list_2_title_index_and_title_id_list_tuple_list(title_list=stopword_removed_title_list, word_map_tuple_list=word_map_tuple_list, title_id_file_save_directory=title_id_file)
    logging.info(f"title_index_and_title_id_list_tuple_list[0:10]: {title_index_and_title_id_list_tuple_list[0:10]}")
    logging.info(f"title_index_and_title_id_list_tuple_list[0][0]: {title_index_and_title_id_list_tuple_list[0][0]}")
    word_key_value_pair_tuple_list = cosine_computer.title_index_and_title_id_list_tuple_list_2_word_key_value_pair_tuple_list(title_index_and_title_id_list_tuple_list=title_index_and_title_id_list_tuple_list)
    logging.info(f"word_key_value_pair_tuple_list[0]: {word_key_value_pair_tuple_list[0]}")
    logging.info(f"word_key_value_pair_tuple_list[0:5]: {word_key_value_pair_tuple_list[0:5]}")
    logging.info(f"word_key_value_pair_tuple_list[0][0]: {word_key_value_pair_tuple_list[0][0]}")
    similarity_trigram_tuple_list = cosine_computer.compute_title_similarity(id_title_tuple_2d_list=word_key_value_pair_tuple_list)
    logging.info(f"len(similarity_trigram_tuple_list): {len(similarity_trigram_tuple_list)}")
    logging.info(f"similarity_trigram_tuple_list[0]: {similarity_trigram_tuple_list[0]}")
    filtered_similarity_trigram_tuple_list = filter(lambda trigram_tuple: trigram_tuple[2] != 0, similarity_trigram_tuple_list)
    sorted_similarity_trigram_tuple_list = sorted(filtered_similarity_trigram_tuple_list, key=lambda trigram_tuple: -trigram_tuple[2])
    logging.info(f"sorted_similarity_trigram_tuple_list[0]: {sorted_similarity_trigram_tuple_list[0]}")
    logging.info(f"sorted_similarity_trigram_tuple_list[1]: {sorted_similarity_trigram_tuple_list[1]}")
    cosine_computer.save_compute_similarity_result(sorted_similarity_trigram_tuple_list=sorted_similarity_trigram_tuple_list, cosine_similarity_result_file_save_directory=cosine_similarity_result_file)
if __name__ == "__main__":
    main()