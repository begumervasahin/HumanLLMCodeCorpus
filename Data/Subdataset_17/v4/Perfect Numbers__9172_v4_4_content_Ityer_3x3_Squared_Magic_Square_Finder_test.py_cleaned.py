import pickle
def remove_duplicates(lst):
    if lst:
        lst.sort()
        unique_list = [lst[-1]]
        for i in range(len(lst)-2, -1, -1):
            if lst[i] != unique_list[0]:
                unique_list.insert(0, lst[i])
    return unique_list
with open("Fail.txt", 'rb') as file:
    list_data = pickle.load(file)
print("Original length:", len(list_data))
list_data = remove_duplicates(list_data)
print("Length after removing duplicates:", len(list_data))