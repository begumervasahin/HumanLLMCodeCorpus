import sys
import os
import shlex
project = 'One-Time Pad'
author = 'Alfio E. Fresta'
copyright = '2016, Alfio E. Fresta'
version = '0.1'
release = '0.1.0a'
extensions = [
    'sphinx.ext.imgmath',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'classic'
html_static_path = ['_static']
htmlhelp_basename = 'otpdoc'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
}
latex_documents = [
    (master_doc, 'otp.tex', 'One-Time Pad Documentation',
     'Alfio E. Fresta', 'manual'),
]
man_pages = [
    (master_doc, 'otp', 'One-Time Pad Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'otp', 'One-Time Pad Documentation',
     author, 'otp', 'One-Time Pad',
     'Miscellaneous'),
]
imgmath_font_size = 11