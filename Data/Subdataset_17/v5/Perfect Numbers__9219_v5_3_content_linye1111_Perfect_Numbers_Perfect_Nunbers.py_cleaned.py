import time
def factors(num):
    factor_list = []
    unique_factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factor_list.append(i)
            num
            i = 2
        else:
            i += 1
    for i in range(len(factor_list)):
        product = factor_list[i]
        for j in range(i + 1, len(factor_list)):
            product *= factor_list[j]
            if product not in factor_list:
                factor_list.append(product)
    unique_factors = list(sorted(set(factor_list)))
    return [1] + unique_factors
def find_special_number():
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
            print(f"Time taken: {time.time() - start} seconds")
            print(f"Special number: {i}")
            break
        i += step
        step += 1
find_special_number()