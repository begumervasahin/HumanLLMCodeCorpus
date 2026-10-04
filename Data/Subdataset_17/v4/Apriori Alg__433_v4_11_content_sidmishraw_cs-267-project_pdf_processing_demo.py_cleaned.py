
__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
import json
import pdb
from pprint import pprint
from pdf_processing import (
    extract_pages,
    extract_page_contents,
    get_pdf_contents,
    create_json_file,
    extract_words,
    build_pdf_json,
    cleanse_extracted_words,
    cleansed_pdf_json,
)
from pdf_processing.pdf_processor import TEST_PDF, TEST_PDF_2
def process_pdf(doc_name, output_file_prefix):
    print(f'Processing PDF: {doc_name}')
    get_pdf_contents(doc_name)
    words_dict = extract_words()
    with open(f'{output_file_prefix}_raw.json', 'w') as file:
        json.dump(words_dict, file)
    cleansed_words_dict = cleanse_extracted_words(words_dict)
    with open(f'{output_file_prefix}_cleansed.json', 'w') as file:
        json.dump(cleansed_words_dict, file)
def process_grouped_pdf(doc_name, output_file_prefix):
    print(f'Processing grouped PDF: {doc_name}')
    get_pdf_contents(doc_name)
    grouped_words_dict = build_pdf_json()
    with open(f'{output_file_prefix}_grouped_raw.json', 'w') as file:
        json.dump(grouped_words_dict, file)
    cleansed_grouped_words_dict = cleansed_pdf_json(grouped_words_dict)
    with open(f'{output_file_prefix}_grouped_cleansed.json', 'w') as file:
        json.dump(cleansed_grouped_words_dict, file)
if __name__ == '__main__':
    print('Converting PDFs into JSONs and making your life simpler...')
    process_pdf(TEST_PDF, 'phase3_1')
    process_grouped_pdf(TEST_PDF_2, 'phase3_2')