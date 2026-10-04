def generate_binary_strings(n, k):
    def backtrack(index, ones_count, current_string):
        if index == n:
            print(''.join(current_string))
            return
        current_string.append('0')
        backtrack(index + 1, ones_count, current_string)
        current_string.pop()
        if ones_count < k:
            current_string.append('1')
            backtrack(index + 1, ones_count + 1, current_string)
            current_string.pop()
    backtrack(0, 0, [])
generate_binary_strings(4, 1)