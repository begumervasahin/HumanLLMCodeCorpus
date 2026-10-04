from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
file_count = {}
list=[]
for line in sys.stdin:
	line = line.strip()
	list.append(line)
	var2, var1 = line.split(',')
	var3, word = var2.split('=')
	word=word.strip()
	var4= var1.split("&")
	count=var4[3]
	count=count.strip()
	try:
		count = int(count)
	except ValueError:
		continue
	if current_word == word:
		current_count += count
	else:
		if current_word:
			file_count[current_word]= current_count
		current_count = count
		current_word = word
if current_word == word:
	file_count[current_word]= current_count
for line in list:
	line = line.strip()
	var2, var1 = line.split(',')
	var3, word = var2.split('=')
	word=word.strip()
	var4, var5= var1.split("=")
	value = var5.split("&")
	file_name= value[0]
	n= value[1]
	total=value[2]
	total_file_count=str(file_count[word])
	print "key="+word+"&"+file_name+", value="+n+"&"+total+"&"+total_file_count