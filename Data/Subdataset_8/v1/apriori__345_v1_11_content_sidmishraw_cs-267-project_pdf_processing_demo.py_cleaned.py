from pprint import pprint
from json import dumps, loads
from pdf_processing import (
    extract_pages, extract_page_contents, get_pdf_contents,
    create_json_file, extract_words, build_pdf_json,
    cleanse_extracted_words, cleansed_pdf_json,
    TEST_PDF, TEST_PDF_2
)
if __name__ == '__main__':
    '''
    Using the pdf `obscalculi_testing_pdf_conv.pdf` as the sample for the demo.
    '''
    print('Converting pdfs into JSONs and making your life simpler...')
    doc_name = TEST_PDF
    get_pdf_contents(TEST_PDF)
    def_dict = extract_words()
    with open('phase3_1.json', 'w') as fp_open:
        fp_open.write(dumps(def_dict))
    def_dict = cleanse_extracted_words(def_dict)
    with open('phase3.json', 'w') as fp_open:
        fp_open.write(dumps(def_dict))
    doc_name = TEST_PDF_2
    get_pdf_contents(TEST_PDF_2)
    def_dict = build_pdf_json()
    with open('phase3_2_1.json', 'w') as fp_open:
        fp_open.write(dumps(def_dict))
    def_dict = cleansed_pdf_json(def_dict)
    with open('phase3_2.json', 'w') as fp_open:
        fp_open.write(dumps(def_dict))