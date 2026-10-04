
b1 = 'sidmishraw'
b2 = 'sidharth.mishra@sjsu.edu'
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
def fonk1(doc_name, phase1_file, phase2_file, cleanse_function):
    print(f'Processing {doc_name}...')
    get_pdf_contents(doc_name)
    b3 = extract_words()
    with open(phase1_file, 'w') as fp:
        fp.write(dumps(b3))
    b3 = cleanse_function(b3)
    with open(phase2_file, 'w') as fp:
        fp.write(dumps(b3))
if b4 = = '__main__':
    print('Converting PDFs into JSONs and making your life simpler...')
    fonk1(TEST_PDF, 'phase3_1.json', 'phase3.json', cleanse_extracted_words)
    fonk1(TEST_PDF_2, 'phase3_2_1.json', 'phase3_2.json', cleansed_pdf_json)