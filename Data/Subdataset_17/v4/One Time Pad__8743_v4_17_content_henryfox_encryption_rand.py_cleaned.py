import random
def generate_random_number(digits):
    nums = [str(random.randint(0, 9)) for _ in range(digits)]
    return "".join(nums)
print(generate_random_number(5))
