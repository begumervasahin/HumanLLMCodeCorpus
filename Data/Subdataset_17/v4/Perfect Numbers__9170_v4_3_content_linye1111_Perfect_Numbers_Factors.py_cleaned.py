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
    print("Initial factors:", factor_list)
    print("Number of factors:", len(factor_list), "Sum of factors:", sum(factor_list))
    for i in range(len(factor_list) - 1):
        product = factor_list[i]
        for j in range(i + 1, len(factor_list)):
            combined_product = factor_list[i] * factor_list[j]
            if combined_product not in factor_list:
                factor_list.append(combined_product)
            product *= factor_list[j]
            if product not in factor_list:
                factor_list.append(product)
    for x in factor_list:
        if x not in unique_factors:
            unique_factors.append(x)
    return [1] + unique_factors
if __name__ == "__main__":
    start_time = time.time()
    num = 33550336
    print("Factors of", num, ":", factors(num))
    print("Execution time:", time.time() - start_time)