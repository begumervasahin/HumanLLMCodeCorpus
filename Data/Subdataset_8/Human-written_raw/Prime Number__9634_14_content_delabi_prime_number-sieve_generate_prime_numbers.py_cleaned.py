def generate_prime_numbers(n):
	if n != None:
		print "Hallo"
		if n > 0:
			if isinstance(n, int):
				if n == 0:
					return[0]
				elif n == 2:
					return[2]
				elif n < 2:
					return []
				s = range (3, n+1, 2)
				mroot = n ** 0.5
				half = (n+1)/2-1
				i = 0
				m = 3
				while  m <= mroot:
					if s[i]:
						j = (m*m-3)/2
						s[j] = 0
						while j < half:
							s[j] = 0
							j+=m
					i = i + 1
					m = 2 * i +3
				return [2] + [x for x in s if x]
			print "That is not an integer. Please enter a number without a decimal"
			return "That is not an integer. Please enter a number without a decimal"
		print "Please enter a positive integer"
		return "Please enter a positive integer"
	print "Please enter a positve integer as the limit!"
	return "Please enter a positve integer as the limit!"