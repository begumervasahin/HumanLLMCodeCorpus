import sys
import os
b1 = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your"
b2 = []
b2 = b1.split(",")
b3 = os.environ['map_input_file']
head, b4 = os.path.split(b3)
b5 = b4
for b6 in sys.stdin:
    b6 = b6.strip()
    b7 = b6.split()
    for word in b7:
		a1 = 0
		for stop in b2:
			if word.lower()==stop.lower():
				a1 = 1
				break
		if a1 = =0:
			print '%s&%s\t%s' % (word,b5, 1)