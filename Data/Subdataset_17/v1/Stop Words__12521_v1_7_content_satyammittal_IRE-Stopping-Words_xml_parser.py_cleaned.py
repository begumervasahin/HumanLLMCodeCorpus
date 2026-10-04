import xml.etree.ElementTree as etree
import time
import os
import operator
PATH_WIKI_XML = ''
FILENAME_WIKI = 'idwiki-20170801-pages-meta-current.xml'
pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
totalCount = 0
articleCount = 0
redirectCount = 0
templateCount = 0
title = None
start_time = time.time()
def strip_tag_name(t):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t
counter = {}
number = 0
check_word = {}
check_doc = {}
for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
    number += 1
    check_word = {}
    if number > 500000:
        break
    tname = strip_tag_name(elem.tag)
    if event == 'start':
        if tname == 'page':
            title = ''
            id = -1
            redirect = ''
            inrevision = False
            ns = 0
        elif tname == 'revision':
            inrevision = True
        else:
            if tname == 'title':
                title = elem.text
            elif tname == 'redirect':
                redirect = elem.attrib['title']
            elif tname == 'text':
                text = elem.text
                if text is not None:
                    for word in text.split():
                        counter[word] = counter.get(word, 0) + 1
                        check_word[word] = check_word.get(word, 0) + 1
        for word in check_word:
            check_doc[word] = check_doc.get(word, 0) + 1
result = {}
for word in check_doc:
    result[word] = counter[word] * check_doc[word]
sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
top_n = 50
for word, count in sorted_counter[:top_n]:
    print(f"{word}: {count}")
print(f"Elapsed time: {time.time() - start_time} seconds")