import zns
from db import primes as RealPrimes
def sieve(N):
	primes = [2]
	state = [-1]*2 + [0]*(N)
	prime_i = 0
	p = 2
	upto = 2
	while p**2 < N:
		print(" -- %d -- " % p)
		for i in range(primes[prime_i-1]**2 if prime_i else p+1, p**2):
			if state[i] == 0:
				print("new ^2 prime:", i)
				primes.append(i)
		print(" -- %d**2 -- " % p)
		for e,q in enumerate(primes[:prime_i]):
			l = zns.lcm(e)
			for i in range(upto + (q - (upto % q)), min(p**3, N+1), q):
				if state[i] == 0:
					if q > 3:
						print("  %d] new: %d = %d*(%d[%d])  {[%d] <-- missing note}" % (q,i,q,l,(i
				state[i] = q
			if q > 3:
				print()
			else:
				print("  %d] ...\n" % q)
		for q in primes[prime_i:]:
			l = q*p
			if q > p**2:
				print("uh oh, breaking because while marking cubethm composites got a %d > %d" % (q, p**2))
				break
			if l > N:
				continue
			assert l < p**3
			if state[l] == 0:
				print("  [%d*%d = %d]" % (p,q,l))
			state[l] = p
		if p**3 < N:
			print("  [%d**3 = %d]" % (p, p**3))
			state[p**3] = p
		upto = p**3
		print(" -- %d**3 -- " % p)
		prime_i += 1
		p = primes[prime_i]
		print("-"*22)
		assert RealPrimes[:len(primes)] == primes or len(primes) > len(RealPrimes)
sieve(15000)