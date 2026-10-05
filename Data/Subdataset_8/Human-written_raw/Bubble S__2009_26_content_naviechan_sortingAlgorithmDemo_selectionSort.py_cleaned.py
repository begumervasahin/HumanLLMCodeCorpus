import math
class selectionSort:
	def __init__(self, lst, trace_mode):
		self.lst = lst
		self.trace_mode = trace_mode
	def sort(self):
		start_idx = 0
		lst = self.lst
		while start_idx < len(lst):
			min_val = lst[start_idx]
			min_idx = start_idx
			for i, elm in enumerate(lst[start_idx : ]):
				if elm < min_val:
					min_val = elm
					min_idx = i + start_idx
			lst[start_idx], lst[min_idx] = lst[min_idx], lst[start_idx]
			if (self.trace_mode):
				self.display_list(lst, start_idx, min_idx)
			start_idx += 1
		return lst
	def display_list(self, lst, i, j):
		lst = [str(k) for k in lst]
		output = '|'
		for k, elm in enumerate(lst):
			if (k == i or k == j):
				elm = elm + '*'
			output = output + ' ' + str(elm) + ' |'
		print(output)
		raw_input("Press Enter to continue...")