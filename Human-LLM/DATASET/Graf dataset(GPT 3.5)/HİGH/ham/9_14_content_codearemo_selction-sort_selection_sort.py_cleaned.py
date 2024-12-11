def selection_sort (items):
	for step in range(len(items)):
		b1 = step
		for location in range(step, len(items)):
			if items[b1] < items[location]:
				b2 = items[b1]
			else:
				b2 = items[location]
				b3 = items[b1]
				items[b1] = b2
				items[location] = b3
	print (items)
	print('Total Number of items  ', len(items))