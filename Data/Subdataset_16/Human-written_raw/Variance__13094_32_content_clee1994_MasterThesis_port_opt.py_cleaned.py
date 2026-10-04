def fonk1(ret_series, base_value):
	import numpy as np
	b1 = np.zeros([len(ret_series)+1])
	b1[0] = base_value
	for i in range(len(ret_series)):
		if np.isnan(ret_series[i]):
			b1[i+1] = b1[i]
		else:
			b1[i+1] = b1[i] * np.exp(ret_series[i])
	return b1
def fonk2(x):
	import numpy as np
	return np.all(np.linalg.eigvals(x) > 0)
def fonk3(mu, b7, b13, b12, h):
	from cvxpy import quad_form, Variable, sum_entries, Problem, Maximize, norm
	from sklearn.covariance import shrunk_covariance
	import numpy as np
	b2 = len(mu)
	b3 = Variable(b2)
	b4 = mu.T*b3
	if fonk2(b7):
		b5 = quad_form(b3, b7)
	else:
		for i in np.linspace(0.01,10000,1000000):
			b6 = shrunk_covariance(b7, shrinkage=i)
			if fonk2(b6):
				b7 = b6
				break
		if not fonk2(b7):
			print('Here you got a serious problem', b8 = True)
			print(b7)
			b9 = np.empty((len(mu)))
			b9[:] = np.nan
			b10 = np.nan
			b11 = np.nan
			return b9, b10, b11
		b5 = quad_form(b3, b7)
	if b12 = = None:
		if b13 = = None:
			b14 = Problem(Maximize(b4 - b5), [sum_entries(b3) == 1, b3 >= h])
		else:
			b14 = Problem(Maximize(b4 - b5), [sum_entries(b3) == 1, b3 >= h,
				b4 = =b13])
	else:
		if b13 = = None:
			b14 = Problem(Maximize(b4 - b5 - b12*norm(b3,1) ),
				[sum_entries(b3) == 1, b3 >= h])
		else:
			b14 = Problem(Maximize(b4 - b5 - b12*norm(b3,1)),
				[sum_entries(b3) == 1, b3 >= h, b4 = =b13])
	b14.solve()
	try:
		b9 = b3.value
		b10 = b4.value
		b11 = b5.value
	except:
		b9 = np.empty((len(mu)))
		b9[:] = np.nan
		b10 = np.nan
		b11 = np.nan
	return b9, b10, b11