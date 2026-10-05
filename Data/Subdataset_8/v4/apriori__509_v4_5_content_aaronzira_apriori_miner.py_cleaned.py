import sys
import apriori
def main():
    if len(sys.argv) < 3:
        print_usage()
    else:
        data_file = sys.argv[1]
        output_file = sys.argv[2]
        sigma, min_set_size = get_optional_parameters()
        print(f"Setting sigma to {sigma} and minimum set size to {min_set_size}.")
        AP = apriori.APriori(data=data_file, out=output_file)
        AP.find_frequent(sigma, min_set_size)
def print_usage():
    print("Expected format: python miner.py <data> <out file> <OPTIONAL sigma> <OPTIONAL min set size>")
def get_optional_parameters():
    sigma = 4
    min_set_size = 3
    if len(sys.argv) >= 4:
        try:
            sigma = int(sys.argv[3])
            if len(sys.argv) >= 5:
                min_set_size = int(sys.argv[4])
        except ValueError:
            print("Optional parameters must be integers. Using default values.")
    return sigma, min_set_size
if __name__ == "__main__":
    main()