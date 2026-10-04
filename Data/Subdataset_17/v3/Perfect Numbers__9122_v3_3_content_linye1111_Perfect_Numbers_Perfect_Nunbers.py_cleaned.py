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
    for i in range(len(factor_list)):
        product = factor_list[i]
        for j in range(i + 1, len(factor_list)):
            y = factor_list[i] * factor_list[j]
            if y not in factor_list:
                factor_list.append(y)
            product *= factor_list[j]
            if product not in factor_list:
                factor_list.append(product)
    unique_factors = list(set(factor_list))
    return [1] + unique_factors
def main():
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
if __name__ == "__main__":
    main()