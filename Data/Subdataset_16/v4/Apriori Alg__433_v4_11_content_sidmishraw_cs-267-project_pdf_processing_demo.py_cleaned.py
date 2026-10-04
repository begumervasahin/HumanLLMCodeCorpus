
b1 = 'sidmishraw'
b2 = 'sidharth.mishra@sjsu.edu'
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
def fonk1(doc_name, output_file_prefix):
    print(f'Processing PDF: {doc_name}')
    get_pdf_contents(doc_name)
    b3 = extract_words()
    with open(f'{output_file_prefix}_raw.json', 'w') as file:
        json.dump(b3, file)
    b4 = cleanse_extracted_words(b3)
    with open(f'{output_file_prefix}_cleansed.json', 'w') as file:
        json.dump(b4, file)
def fonk2(doc_name, output_file_prefix):
    print(f'Processing grouped PDF: {doc_name}')
    get_pdf_contents(doc_name)
    b5 = build_pdf_json()
    with open(f'{output_file_prefix}_grouped_raw.json', 'w') as file:
        json.dump(b5, file)
    b6 = cleansed_pdf_json(b5)
    with open(f'{output_file_prefix}_grouped_cleansed.json', 'w') as file:
        json.dump(b6, file)
if b7 = = '__main__':
    print('Converting PDFs into JSONs and making your life simpler...')
    fonk1(TEST_PDF, 'phase3_1')
    fonk2(TEST_PDF_2, 'phase3_2')