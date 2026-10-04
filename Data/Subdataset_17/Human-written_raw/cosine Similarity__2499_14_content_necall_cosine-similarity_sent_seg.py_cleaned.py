import nltk
import os
def remove_non_ASCII(content):
    content_printable_list=[c for c in content if (32 <= ord(c) and ord(c) <= 126)]
    return ''.join(content_printable_list)
def collect_all_sentences(text_lines,sentence_splitter):
	print "num lines:", len(text_lines)
	sentences_tok=[]
	line_count=0
	for content in text_lines:
		line_count+=1
		if(line_count%1000==0):
			print float(line_count)/len(text_lines)
		content_printable=remove_non_ASCII(content)
		content_printable=content_printable.replace("Mr .","Mr")
		sentences_raw = sentence_splitter.sentences_from_text(content_printable)
		for sent in sentences_raw:
			sentences_tok.append(sent)
	return sentences_tok
PATH_TO_DATA="/Users/ken77921/Desktop/TA/2004,7-05_nyt_tok"
with open(os.path.join(PATH_TO_DATA),'r') as doc:
	text_lines = doc.readlines()
sentence_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
sentences_tok=collect_all_sentences(text_lines,sentence_splitter)
f_out_path="/Users/ken77921/Desktop/TA/2004,7-05_nyt_sent"
f_out=open(f_out_path,"w")
for sent in sentences_tok:
	f_out.write(sent+"\n")
f_out.close()