import sys
import apriori
def parse_arguments():
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <data> <out file> <OPTIONAL sigma> <OPTIONAL min set size>")
        sys.exit(1)
    data = sys.argv[1]
    out_file = sys.argv[2]
    sigma = 4
    min_set_size = 3
    if len(sys.argv) >= 5:
        try:
            sigma = int(sys.argv[3])
            min_set_size = int(sys.argv[4])
        except ValueError:
            print("Sigma and minimum set size must be integers. Using default values.")
    return data, out_file, sigma, min_set_size
def main():
    data, out_file, sigma, min_set_size = parse_arguments()
    print(f"Setting sigma to {sigma} and minimum set size to {min_set_size}.")
    ap = apriori.APriori(data=data, out=out_file)
    ap.find_frequent(sigma, min_set_size)
if __name__ == "__main__":
    main()