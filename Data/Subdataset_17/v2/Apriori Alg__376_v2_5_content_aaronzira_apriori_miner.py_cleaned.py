import sys
import apriori
def main():
    if len(sys.argv) < 3:
        print("Usage: python miner.py <data> <out file> [<OPTIONAL sigma> <OPTIONAL min set size>]")
        return
    data = sys.argv[1]
    out_file = sys.argv[2]
    sigma = 4
    min_set_size = 3
    try:
        if len(sys.argv) > 3:
            sigma = int(sys.argv[3])
        if len(sys.argv) > 4:
            min_set_size = int(sys.argv[4])
    except ValueError:
        print("Invalid format for sigma or minimum set size. Using default values.")
    print(f"Setting sigma to {sigma} and minimum set size to {min_set_size}.")
    AP = apriori.APriori(data=data, out=out_file)
    AP.find_frequent(sigma, min_set_size)
if __name__ == "__main__":
    main()