import pickle
def remove_duplicates(lst):
    if lst:
        lst.sort()
        last = lst[-1]
        for i in range(len(lst) - 2, -1, -1):
            if last == lst[i]:
                del lst[i]
            else:
                last = lst[i]
    return lst
def save_to_file(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
def main():
    sample_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    save_to_file(sample_list, "sample_list.pkl")
    sample_list = load_from_file("sample_list.pkl")
    print("Length before removing duplicates:", len(sample_list))
    sample_list = remove_duplicates(sample_list)
    print("Length after removing duplicates:", len(sample_list))
if __name__ == '__main__':
    main()