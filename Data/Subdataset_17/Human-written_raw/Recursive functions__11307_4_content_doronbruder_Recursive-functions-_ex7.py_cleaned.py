def toString(List):
    return ''.join(List)
def print_to_n(n):
    if n >= 1:
        print_to_n(n - 1)
        print(str(n))
    else:
        return
def print_reversed(n):
    if n >= 1:
        print(str(n))
        print_reversed(n - 1)
def has_divisor_smaller_than(n, i):
    if i == 1 or i==0:
        return False
    elif n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)
def is_prime(n):
    if n<2:
        return False
    i=int(n**0.5)
    if has_divisor_smaller_than(n, i) == False:
        return True
    return False
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
def exp_n_x(n, x):
    if n == 0:
        return 1
    return (x ** n) / factorial(n) + exp_n_x(n - 1, x)
def play_hanoi(hanoi, n, src, dest, temp):
    if n<1:
        return
    elif n == 1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)
def print_sequences(char_list,n):
    if n==0:
        return
    k=n
    n = len(set(char_list))
    print_sequences_rec(char_list, "", n, k)
def print_sequences_rec(char_list, prefix, n, k):
    if (k == 0):
        print(prefix)
        return
    for i in range(n):
        newPrefix = prefix + char_list[i]
        print_sequences_rec(char_list, newPrefix, n, k - 1)
def print_no_repetition_sequences(char_list, n):
    if n==0:
        return
    print_no_reptition_sequences_rec(char_list, "", n)
def print_no_reptition_sequences_rec(char_list, prefix, n):
    if (n == 0):
        print(prefix)
        return
    for i, char in enumerate(char_list):
        new_prefix=prefix+char
        print_no_reptition_sequences_rec(char_list[:i]+char_list[i+1:],new_prefix, n-1)
def parentheses(n):
    str=[""]*2*n
    results_lst=[]
    if(n > 0):
        parentheses_rec(str, 0, n, 0, 0, results_lst)
    return results_lst
def parentheses_rec(str, pos, n, open, close, results_lst):
    if (close == n):
        x=""
        for i in str:
            x+=i
        results_lst.append(x)
        return
    else:
        if (open > close):
            str[pos] = ')'
            parentheses_rec(str, pos + 1, n, open, close + 1, results_lst)
        if (open < n):
            str[pos] = '('
            parentheses_rec(str, pos + 1, n, open + 1, close, results_lst)
def up_and_right(n,k):
    if k==0 and n==0:
        return None
    if n<0 or k<0:
        return None
    up_and_right_rec(n, k,"")
def up_and_right_rec(n, k,prefix=''):
    if n == 0 and k == 0:
        print(prefix)
        return
    elif  n== 0:
        up_and_right_rec(n, k-1, prefix+'u')
        return
    elif k==0 :
        up_and_right_rec(n-1, k, prefix+'r')
        return
    up_and_right_rec(n, k - 1, prefix +'u')
    up_and_right_rec(n-1, k, prefix +'r')
def flood_fill(image, start):
    """This function  changes every "." which is right after the start point or to  another "." in one of four
    directions(up down left or right)
     characters to "*  The main recursive function Starting at point(x , y)  changes any "." when located in above valid places
      to "*"."""
    imageWidth = len(image)
    imageHeight = len(image[0])
    if image[x][y] != empty_char:
        return
    image[x][y] = full_char
    floodFill_rec(image, x - 1, y, empty_char, full_char)
    floodFill_rec(image, x, y - 1, empty_char, full_char)
    floodFill_rec(image, x + 1, y, empty_char, full_char)
    floodFill_rec(image, x, y + 1, empty_char, full_char)