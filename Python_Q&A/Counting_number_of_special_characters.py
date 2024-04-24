st = input("Enter any string: ")

import string
lower_and_upper_cases = string.ascii_letters
count = 0
for i in st:
    if i  in lower_and_upper_cases:
        continue
    count = count + 1

print(count)        