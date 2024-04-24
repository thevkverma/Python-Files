st = input(("Enter any String: "))

count = 0
v = 'aeiouAEIOU'
for i in st:
    if i in v:
         count = count + 1
print(count)    