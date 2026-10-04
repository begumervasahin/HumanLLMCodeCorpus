
__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
import json
from pdf_processing import (
    get_pdf_contents,
    extract_words,
    cleanse_extracted_words,
    build_pdf_json,
    cleansed_pdf_json,
)
from pdf_processing.pdf_processor import TEST_PDF, TEST_PDF_2
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
def process_pdf(doc_name, output_file_prefix):
    print(f'Processing PDF: {doc_name}')
    get_pdf_contents(doc_name)
    words_dict = extract_words()
    save_to_json(words_dict, f'{output_file_prefix}_raw.json')
    cleansed_words_dict = cleanse_extracted_words(words_dict)
    save_to_json(cleansed_words_dict, f'{output_file_prefix}_cleansed.json')
def process_grouped_pdf(doc_name, output_file_prefix):
    print(f'Processing grouped PDF: {doc_name}')
    get_pdf_contents(doc_name)
    grouped_words_dict = build_pdf_json()
    save_to_json(grouped_words_dict, f'{output_file_prefix}_grouped_raw.json')
    cleansed_grouped_words_dict = cleansed_pdf_json(grouped_words_dict)
    save_to_json(cleansed_grouped_words_dict, f'{output_file_prefix}_grouped_cleansed.json')
def main():
    print('Converting PDFs into JSONs and making your life simpler...')
    process_pdf(TEST_PDF, 'phase3_1')
    process_grouped_pdf(TEST_PDF_2, 'phase3_2')
if __name__ == '__main__':
    main()