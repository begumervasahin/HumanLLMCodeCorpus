from pprint import pprint
from json import dumps
from pdf_processing import (
    extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    get_pdf_contents, TEST_PDF, TEST_PDF_2
)
def inform_user(message):
    print(message)
if __name__ == '__main__':
    inform_user('Converting PDFs into JSONs and simplifying your life...')
    get_pdf_contents(TEST_PDF)
    word_dict = extract_words()
    with open('phase3_1.json', 'w') as json_file:
        json_file.write(dumps(word_dict))
    word_dict = cleanse_extracted_words(word_dict)
    with open('phase3.json', 'w') as json_file:
        json_file.write(dumps(word_dict))
    get_pdf_contents(TEST_PDF_2)
    pdf_dict = build_pdf_json()
    with open('phase3_2_1.json', 'w') as json_file:
        json_file.write(dumps(pdf_dict))
    pdf_dict = cleansed_pdf_json(pdf_dict)
    with open('phase3_2.json', 'w') as json_file:
        json_file.write(dumps(pdf_dict))