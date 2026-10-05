import sys
from apriori import APriori
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Expected format: python miner.py <data> <out file> <OPTIONAL sigma> <OPTIONAL min set size>")
    else:
        data_file = sys.argv[1]
        output_file = sys.argv[2]
        sigma = 4
        min_set_size = 3
        if len(sys.argv) >= 4:
            try:
                sigma = int(sys.argv[3])
                if len(sys.argv) >= 5:
                    min_set_size = int(sys.argv[4])
            except ValueError:
                print("Optional parameters must be integers. Using default values.")
        print(f"Setting sigma to {sigma} and minimum set size to {min_set_size}.")
        apriori = APriori(data=data_file, out=output_file)
        apriori.find_frequent(sigma, min_set_size)