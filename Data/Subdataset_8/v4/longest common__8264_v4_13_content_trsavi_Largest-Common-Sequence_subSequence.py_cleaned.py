def sub_sequence(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    result1 = []
    result2 = []
    if len(string1) <= len(string2):
        shorter = string1
        longer = string2
    else:
        shorter = string2
        longer = string1
    for j in range(0, len(shorter) + 1):
        for char in shorter[j:]:
            if char in longer[index:]:
                result1.append(char)
                index = longer[index:].index(char)
        index = 0
        for char in result1:
            if (result1.count(char) > shorter.count(char) or
                    result1.count(char) > longer.count(char)):
                result1 = []
        if len(result1) >= len(result2):
            result2 = result1
            result1 = []
        else:
            result1 = []
    longest_subsequence = ''.join(result2)
    return longest_subsequence