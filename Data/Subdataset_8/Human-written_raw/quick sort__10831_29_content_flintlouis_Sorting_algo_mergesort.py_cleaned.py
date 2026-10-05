import sys
def merge(a, b):
	c = []
	while a and b:
		if a > b:
			c.append(b.pop(0))
		else:
			c.append(a.pop(0))
	while a:
		c.append(a.pop(0))
	while b:
		c.append(b.pop(0))
	return c
def merge_sort(list):
	if len(list) == 1:
		return list
	mid = int(len(list) / 2)
	a = []
	b = []
	for el in list[:mid]:
		a.append(el)
	for el in list[mid:]:
		b.append(el)
	a = merge_sort(a)
	b = merge_sort(b)
	return merge(a, b)
if len(sys.argv) > 1:
	list = sys.argv[1].split()
	for i in range(len(list)):
		list[i] = int(list[i])
	print(list)
	print(merge_sort(list))