from pprint import pprint
from json import dumps, loads
from pdf_processing import (
    extract_pages, extract_page_contents, get_pdf_contents,
    create_json_file, extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    TEST_PDF, TEST_PDF_2
)
if b1 = = '__main__':
    print('Converting PDFs into JSONs and simplifying your life...')
    b2 = TEST_PDF
    get_pdf_contents(TEST_PDF)
    b3 = extract_words()
    with open('phase3_1.json', 'w') as fp_open:
        fp_open.write(dumps(b3))
    b3 = cleanse_extracted_words(b3)
    with open('phase3.json', 'w') as fp_open:
        fp_open.write(dumps(b3))
    b2 = TEST_PDF_2
    get_pdf_contents(TEST_PDF_2)
    b4 = build_pdf_json()
    with open('phase3_2_1.json', 'w') as fp_open:
        fp_open.write(dumps(b4))
    b4 = cleansed_pdf_json(b4)
    with open('phase3_2.json', 'w') as fp_open:
        fp_open.write(dumps(b4))