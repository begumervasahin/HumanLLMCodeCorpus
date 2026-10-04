
__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
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
def process_pdf(doc_name, phase1_file, phase2_file, cleanse_function):
    print(f'Processing {doc_name}...')
    get_pdf_contents(doc_name)
    def_dict = extract_words()
    with open(phase1_file, 'w') as fp:
        fp.write(dumps(def_dict))
    def_dict = cleanse_function(def_dict)
    with open(phase2_file, 'w') as fp:
        fp.write(dumps(def_dict))
if __name__ == '__main__':
    print('Converting PDFs into JSONs and making your life simpler...')
    process_pdf(TEST_PDF, 'phase3_1.json', 'phase3.json', cleanse_extracted_words)
    process_pdf(TEST_PDF_2, 'phase3_2_1.json', 'phase3_2.json', cleansed_pdf_json)