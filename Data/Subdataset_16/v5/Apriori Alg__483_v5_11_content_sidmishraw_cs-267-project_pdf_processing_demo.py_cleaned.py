
b1 = 'sidmishraw'
b2 = 'sidharth.mishra@sjsu.edu'
import json
from pdf_processing import (
    get_pdf_contents,
    extract_words,
    cleanse_extracted_words,
    build_pdf_json,
    cleansed_pdf_json,
)
from pdf_processing.pdf_processor import TEST_PDF, TEST_PDF_2
def fonk1(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
def fonk2(doc_name, output_file_prefix):
    print(f'Processing PDF: {doc_name}')
    get_pdf_contents(doc_name)
    b3 = extract_words()
    fonk1(b3, f'{output_file_prefix}_raw.json')
    b4 = cleanse_extracted_words(b3)
    fonk1(b4, f'{output_file_prefix}_cleansed.json')
def fonk3(doc_name, output_file_prefix):
    print(f'Processing grouped PDF: {doc_name}')
    get_pdf_contents(doc_name)
    b5 = build_pdf_json()
    fonk1(b5, f'{output_file_prefix}_grouped_raw.json')
    b6 = cleansed_pdf_json(b5)
    fonk1(b6, f'{output_file_prefix}_grouped_cleansed.json')
def fonk4():
    print('Converting PDFs into JSONs and making your life simpler...')
    fonk2(TEST_PDF, 'phase3_1')
    fonk3(TEST_PDF_2, 'phase3_2')
if b7 = = '__main__':
    fonk4()