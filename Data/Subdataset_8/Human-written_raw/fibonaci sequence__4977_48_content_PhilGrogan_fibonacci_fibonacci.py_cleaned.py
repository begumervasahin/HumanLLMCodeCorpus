
current_number = 1
previous_number = 1
total = 0
i = int(input("Enter the number of the fibonacci sequence you want displayed: "))
for x in range(i-1):
    total = current_number + previous_number
    previous_number = current_number
    current_number = total
li = list(str(i))
if li[len(li) - 1] == '1' and li[len(li) - 2] != 1:
    suffix = 'st'
elif li[len(li) - 1] == '2' and li[len(li) - 2] != 1:
    suffix = 'nd'
elif li[len(li) - 1] == '3' and li[len(li) - 2] != 1:
    suffix = 'rd'
else:
    suffix = 'th'
print(f"{current_number:,d} is the {i:,d}{suffix} number of the fibonacci sequence.")