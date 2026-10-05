import os
import logging
from myclass.class_compute_title_similarity import ComputeTitleSimilarity
from myclass.class_get_text_data_from_database import GetTextDataFromDB
def main():
    database_name = "essayDB"
    GetTextData = GetTextDataFromDB(database_name=database_name)
    table_name_list = GetTextData.count_essay_num(database_name=database_name)
    stopword_file_name = "stopword.txt"
    stopword_file_path = "./data/input"
    stopword_file_read_directory = os.path.join(stopword_file_path, stopword_file_name)
    word_map_file_name = "word_map.txt"
    word_map_file_path = "./data/output"
    word_map_file_save_directory = os.path.join(word_map_file_path, word_map_file_name)
    title_id_file_name = "title_id.txt"
    title_id_file_path = "./data/output"
    title_id_file_save_directory = os.path.join(title_id_file_path, title_id_file_name)
    cosine_similarity_result_file_name = "cosine_similarity_result.txt"
    cosine_similarity_result_file_path = "./data/output"
    cosine_similarity_result_file_save_directory = os.path.join(cosine_similarity_result_file_path, cosine_similarity_result_file_name)
    title_list = GetTextData.get_title_list_in_db(database_name=database_name, table_name_list=table_name_list)
    logging.info(f"title_list[1:4]: {title_list[1:4]}")
    logging.info(f"title_list[0]: {title_list[0]}")
    logging.info(f"type(title_list[0]): {type(title_list[0])}")
    logging.info(f"len(title_list): {len(title_list)}")
    logging.info(f"type(title_list): {type(title_list)}")
    CosineComputer = ComputeTitleSimilarity()
    logging.info(f"table_name_list: {table_name_list}")
    word_map_tuple_list = CosineComputer.get_word_map_tuple_list(title_list=title_list, word_map_file_save_directory=word_map_file_save_directory)
    logging.info(f"word_map_tuple_list[:10]: {word_map_tuple_list[:10]}")
    stopword_removed_title_list = CosineComputer.remove_stopword_in_title_list(title_list=title_list, stopword_file_read_directory=stopword_file_read_directory)
    title_index_and_title_id_list_tuple_list = CosineComputer.title_list_2_title_index_and_title_id_list_tuple_list(title_list=stopword_removed_title_list, word_map_tuple_list=word_map_tuple_list, title_id_file_save_directory=title_id_file_save_directory)
    logging.info(f"title_index_and_title_id_list_tuple_list[0:10]: {title_index_and_title_id_list_tuple_list[0:10]}")
    logging.info(f"title_index_and_title_id_list_tuple_list[0][0]: {title_index_and_title_id_list_tuple_list[0][0]}")
    word_key_value_pair_tuple_list = CosineComputer.title_index_and_title_id_list_tuple_list_2_word_key_value_pair_tuple_list(title_index_and_title_id_list_tuple_list=title_index_and_title_id_list_tuple_list)
    logging.info(f"word_key_value_pair_tuple_list[0]: {word_key_value_pair_tuple_list[0]}")
    logging.info(f"word_key_value_pair_tuple_list[0:5]: {word_key_value_pair_tuple_list[0:5]}")
    logging.info(f"word_key_value_pair_tuple_list[0][0]: {word_key_value_pair_tuple_list[0][0]}")
    similarity_trigram_tuple_list = CosineComputer.compute_title_similarity(id_title_tuple_2d_list=word_key_value_pair_tuple_list)
    logging.info(f"len(similarity_trigram_tuple_list): {len(similarity_trigram_tuple_list)}")
    logging.info(f"similarity_trigram_tuple_list[0]: {similarity_trigram_tuple_list[0]}")
    filtered_similarity_trigram_tuple_list = filter(lambda trigram_tuple: trigram_tuple[2] != 0, similarity_trigram_tuple_list)
    sorted_similarity_trigram_tuple_list = sorted(filtered_similarity_trigram_tuple_list, key=lambda trigram_tuple: -trigram_tuple[2])
    logging.info(f"sorted_similarity_trigram_tuple_list[0]: {sorted_similarity_trigram_tuple_list[0]}")
    logging.info(f"sorted_similarity_trigram_tuple_list[1]: {sorted_similarity_trigram_tuple_list[1]}")
    CosineComputer.save_compute_similarity_result(sorted_similarity_trigram_tuple_list=sorted_similarity_trigram_tuple_list, cosine_similarity_result_file_save_directory=cosine_similarity_result_file_save_directory)
if __name__ == "__main__":
    main()