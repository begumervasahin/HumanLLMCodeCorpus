import time
def factors(num):
    factor_list = []
    unique_factors = []
    i = 2
    while i < num:
        if num % i == 0:
            factor_list.append(i)
            num /= i
            i = 2
            continue
        if i == num - 1:
            factor_list.append(int(num))
        i += 1
    length = len(factor_list)
    for i in range(length - 1):
        product = factor_list[i]
        for j in range(i + 1, length):
            combined_product = factor_list[i] * factor_list[j]
            if combined_product not in factor_list:
                factor_list.append(combined_product)
            if not (i == 0 and j == length - 1):
                product *= factor_list[j]
                if product not in factor_list:
                    factor_list.append(product)
    for factor in factor_list:
        if factor not in unique_factors:
            unique_factors.append(factor)
    return [1] + unique_factors
start = time.time()
step = 3
i = 3
print(6)
while True:
    if i % 9 != 1:
        i += step
        step += 1
        continue
    factor_list = factors(i)
    if sum(factor_list) == i:
        print(time.time() - start)
        print(i)
    i += step
    step += 1