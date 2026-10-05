
__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
from pprint import pprint
from json import dumps
from pdf_processing import (
    extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    get_pdf_contents, TEST_PDF, TEST_PDF_2
)
if __name__ == '__main__':
    print('Converting PDFs into JSONs and simplifying your life...')
    doc_name = TEST_PDF
    get_pdf_contents(TEST_PDF)
    word_dict = extract_words()
    with open('phase3_1.json', 'w') as json_file:
        json_file.write(dumps(word_dict))
    word_dict = cleanse_extracted_words(word_dict)
    with open('phase3.json', 'w') as json_file:
        json_file.write(dumps(word_dict))
    doc_name = TEST_PDF_2
    get_pdf_contents(TEST_PDF_2)
    pdf_dict = build_pdf_json()
    with open('phase3_2_1.json', 'w') as json_file:
        json_file.write(dumps(pdf_dict))
    pdf_dict = cleansed_pdf_json(pdf_dict)
    with open('phase3_2.json', 'w') as json_file:
        json_file.write(dumps(pdf_dict))