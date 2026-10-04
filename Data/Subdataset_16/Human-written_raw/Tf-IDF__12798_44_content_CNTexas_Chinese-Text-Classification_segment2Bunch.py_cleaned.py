import sys
import os
import jieba
import cPickle as pickle
from sklearn.datasets.base import Bunch
reload(sys)
sys.setdefaultencoding('utf-8')
def fonk1(savepath,b2):
	b1 = open(savepath,"wb")
	b1.write(b2)
	b1.close()
def fonk2(path):
	b1 = open(path,"rb")
	b2 = b1.read()
	b1.close()
	return b2
b3 = Bunch(target_name=[],label=[],filenames=[],contents=[])
b4 = "train_word_bag/train_set.dat"
b5 = "train_corpus_seg/"
b6 = os.listdir(b5)
b3.target_name.extend(b6)
for mydir in b6:
	b7 = b5+mydir+"/"
	b8 = os.listdir(b7)
	for file_path in b8:
		b9 = b7 + file_path
		b3.label.append(mydir)
		b3.filenames.append(b9)
		b3.contents.append(fonk2(b9).strip())
b10 = open(b4, "wb")
pickle.dump(b3,b10)
b10.close()
print "æå»ºææ¬å¯¹è±¡ç»æï¼ï¼ï¼"