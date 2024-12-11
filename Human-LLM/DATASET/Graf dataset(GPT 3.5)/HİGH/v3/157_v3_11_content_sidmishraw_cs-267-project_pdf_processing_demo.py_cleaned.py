from pprint import pprint
from json import dumps
from pdf_processing import (
    extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    get_pdf_contents, TEST_PDF, TEST_PDF_2
)
def fonk1(message):
    print(message)
if b1 = = '__main__':
    fonk1('Converting PDFs into JSONs and simplifying your life...')
    get_pdf_contents(TEST_PDF)
    b2 = extract_words()
    with open('phase3_1.json', 'w') as json_file:
        json_file.write(dumps(b2))
    b2 = cleanse_extracted_words(b2)
    with open('phase3.json', 'w') as json_file:
        json_file.write(dumps(b2))
    get_pdf_contents(TEST_PDF_2)
    b3 = build_pdf_json()
    with open('phase3_2_1.json', 'w') as json_file:
        json_file.write(dumps(b3))
    b3 = cleansed_pdf_json(b3)
    with open('phase3_2.json', 'w') as json_file:
        json_file.write(dumps(b3))