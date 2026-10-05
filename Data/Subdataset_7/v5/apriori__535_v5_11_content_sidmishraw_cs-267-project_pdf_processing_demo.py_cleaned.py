
b1 = 'sidmishraw'
b2 = 'sidharth.mishra@sjsu.edu'
from pprint import pprint
from json import dumps
from pdf_processing import (
    extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    get_pdf_contents, TEST_PDF, TEST_PDF_2
)
if b3 = = '__main__':
    print('Converting PDFs into JSONs and simplifying your life...')
    b4 = TEST_PDF
    get_pdf_contents(TEST_PDF)
    b5 = extract_words()
    with open('phase3_1.json', 'w') as json_file:
        json_file.write(dumps(b5))
    b5 = cleanse_extracted_words(b5)
    with open('phase3.json', 'w') as json_file:
        json_file.write(dumps(b5))
    b4 = TEST_PDF_2
    get_pdf_contents(TEST_PDF_2)
    b6 = build_pdf_json()
    with open('phase3_2_1.json', 'w') as json_file:
        json_file.write(dumps(b6))
    b6 = cleansed_pdf_json(b6)
    with open('phase3_2.json', 'w') as json_file:
        json_file.write(dumps(b6))