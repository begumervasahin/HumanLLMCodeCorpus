def g(x):
	for i in range(2,x):
		if x % i == 0:
			break
		else:
			if i+1 == x:
				return x
ans = filter(g,range(9,201))
temp = [1]
len_ans = len(ans)
for i in range(0,len_ans):
	z = ans[i]*ans[i]
	if  z < 201:
		temp.append(z)
		for j in range(i,len_ans):
			y = ans[i]*ans[j+1]
			if y < 201:
				temp.append(y)
			else: break
	else: break
print(temp)
ans = ans + temp
ans.sort()
print(ans)
print(len_ans)