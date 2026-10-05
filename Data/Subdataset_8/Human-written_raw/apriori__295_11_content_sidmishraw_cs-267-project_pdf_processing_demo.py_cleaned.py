11. Repository: sidmishraw/cs-267-project
   File: pdf_processing_demo.py
   URL: https:
   Code Content:
__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
'''
This is a demo for the PDF processing module.
'''
from pprint import pprint
from json import dumps
from json import loads
from pdb import set_trace
from pdf_processing import extract_pages
from pdf_processing import extract_page_contents
from pdf_processing import get_pdf_contents
from pdf_processing import create_json_file
from pdf_processing import extract_words
from pdf_processing import build_pdf_json
from pdf_processing import cleanse_extracted_words
from pdf_processing import cleansed_pdf_json
from pdf_processing.pdf_processor import TEST_PDF
from pdf_processing.pdf_processor import TEST_PDF_2
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
   README Content:
Simplicial Complex Text Analysis
![](./thumbnail.png)
* PDF parser
* Word Stemmer
* Apriori modified version
