import time
def factors(num):
    factor_list = []
    unique_factors = []
    i = 2
    while i < num:
        if num % i == 0:
            factor_list.append(i)
            num
            i = 2
            continue
        if i == num - 1:
            factor_list.append(num)
        i += 1
    i = 0
    length = len(factor_list)
    while i < length - 1:
        j = i + 1
        product = factor_list[i]
        while j < length and length > 2:
            y = factor_list[i] * factor_list[j]
            if y not in factor_list:
                factor_list.append(y)
            if not (i == 0 and j == length - 1):
                product *= factor_list[j]
                if product not in factor_list:
                    factor_list.append(product)
            j += 1
        i += 1
    for x in factor_list:
        if x not in unique_factors:
            unique_factors.append(x)
    return [1] + unique_factors
start = time.time()
k = 3
i = 3
print(6)
while True:
    if i % 9 != 1:
        i += k
        k += 1
        continue
    factor_list = factors(i)
    if sum(factor_list) == i:
        print(time.time() - start)
        print(i)
    i += k
    k += 1