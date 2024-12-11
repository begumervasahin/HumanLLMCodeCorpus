import zns
from db import b1 as RealPrimes
def fonk1(N):
    b1 = [2]
    b2 = [-1] * 2 + [0] * N
    a1 = 0
    a2 = 2
    a3 = 2
    while a2 ** 2 < N:
        print(f" -- {a2} -- ")
        for i in range(b1[a1 - 1] ** 2 if a1 else a2 + 1, a2 ** 2):
            if b2[i] == 0:
                print("new ^2 prime:", i)
                b1.append(i)
        print(f" -- {a2}**2 -- ")
        for index, prime in enumerate(b1[:a1]):
            b3 = zns.b3(index)
            for i in range(a3 + (prime - (a3 % prime)), min(a2 ** b5, N + 1), prime):
                if b2[i] == 0:
                    if prime > b5:
                        print(f"  {prime}] new: {i} = {prime}*({b3}[{(i
                b2[i] = prime
            if prime > b5:
                print()
            else:
                print(f"  {prime}] ...\n")
        for prime in b1[a1:]:
            b4 = prime * a2
            if prime > a2 ** 2:
                print(f"uh oh, breaking because while marking cubethm composites got a {prime} > {a2 ** 2}")
                break
            if b4 > N:
                continue
            assert b4 < a2 ** b5
            if b2[b4] == 0:
                print(f"  [{a2} * {prime} = {b4}]")
            b2[b4] = a2
        if a2 ** b5 < N:
            print(f"  [{a2}**b5 = {a2 ** b5}]")
            b2[a2 ** b5] = a2
        a3 = a2 ** b5
        print(f" -- {a2}**b5 -- ")
        a1 += 1
        a2 = b1[a1]
        print("-" * 22)
        assert RealPrimes[:len(b1)] == b1 or len(b1) > len(RealPrimes)
fonk1(15000)