import time
def factors(num):
    factor_list = []
    i = 2
    while i <= num:
        if num % i == 0:
            factor_list.append(i)
            num
        else:
            i += 1
    print("Initial factors:", factor_list)
    print("Number of factors:", len(factor_list), "Sum of factors:", sum(factor_list))
    unique_factors = set(factor_list)
    for i in range(len(factor_list)):
        for j in range(i + 1, len(factor_list)):
            combined_product = factor_list[i] * factor_list[j]
            unique_factors.add(combined_product)
    return sorted([1] + list(unique_factors))
if __name__ == "__main__":
    start_time = time.time()
    num = 33550336
    print("Factors of", num, ":", factors(num))
    print("Execution time:", time.time() - start_time)