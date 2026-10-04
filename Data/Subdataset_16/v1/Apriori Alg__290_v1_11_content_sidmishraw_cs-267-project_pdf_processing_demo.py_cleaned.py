
b1 = 'sidmishraw'
b2 = 'sidharth.mishra@sjsu.edu'
'''
This is a demo for the PDF processing module.
'''
from pprint import pprint
from json import dumps
from pdb import set_trace
from pdf_processing import (
    extract_pages,
    extract_page_contents,
    get_pdf_contents,
    create_json_file,
    extract_words,
    build_pdf_json,
    cleanse_extracted_words,
    cleansed_pdf_json
)
from pdf_processing.pdf_processor import TEST_PDF, TEST_PDF_2
if b3 = = '__main__':
    '''
    Using the pdf `obscalculi_testing_pdf_conv.pdf` as the sample for the demo.
    '''
    print('Converting pdfs into JSONs and making your life simpler...')
    b4 = TEST_PDF
    get_pdf_contents(b4)
    b5 = extract_words()
    with open('phase3_1.json', 'w') as fp_open:
        fp_open.write(dumps(b5))
    b5 = cleanse_extracted_words(b5)
    with open('phase3.json', 'w') as fp_open:
        fp_open.write(dumps(b5))
    b4 = TEST_PDF_2
    get_pdf_contents(b4)
    b5 = build_pdf_json()
    with open('phase3_2_1.json', 'w') as fp_open:
        fp_open.write(dumps(b5))
    b5 = cleansed_pdf_json(b5)
    with open('phase3_2.json', 'w') as fp_open:
        fp_open.write(dumps(b5))