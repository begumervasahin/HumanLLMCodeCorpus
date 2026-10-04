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
def main():
    sample_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    with open("sample_list.pkl", 'wb') as file:
        pickle.dump(sample_list, file)
    with open("sample_list.pkl", 'rb') as file:
        sample_list = pickle.load(file)
    print("Length before removing duplicates:", len(sample_list))
    sample_list = remove_duplicates(sample_list)
    print("Length after removing duplicates:", len(sample_list))
if __name__ == '__main__':
    main()