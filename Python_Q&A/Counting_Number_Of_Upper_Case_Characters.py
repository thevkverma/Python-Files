a = input("Enter any string: ")

count = 0
for i in a:
    if i.isupper():
        count = count+1
print(count)        