import cProfile
def compute_golden_ratio_sequence(n):
    prev_term = 1
    curr_term = 1
    for _ in range(2, n):
        next_term = prev_term + curr_term
        prev_term = curr_term
        curr_term = next_term
        ratio = curr_term / prev_term
        print(ratio)
def main():
    num_terms = 1476
    compute_golden_ratio_sequence(num_terms)
if __name__ == "__main__":
    cProfile.run("main()", filename="profile_results.txt")