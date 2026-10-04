import random
def rand(dig):
	nums = []
	for x in range(0, dig):
		nums.append(str(random.randint(0,9)))
	num = "".join(nums)
	return num