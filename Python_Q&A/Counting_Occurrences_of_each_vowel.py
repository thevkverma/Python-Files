st = input("Enter any String: ")

v = 'aeiou'
d = {}.fromkeys(v,0)
# after printing the value of d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for i in st:
    if i in d:
        d[i] = d[i] + 1
print(d)        