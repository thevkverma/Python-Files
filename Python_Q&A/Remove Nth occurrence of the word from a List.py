mylist = ["geeks", "for", "geeks"]
word = "geeks"
n = 2

count = 0

for i in range(0, len(mylist)):
    if(mylist[i]==word):
        count = count+1
        if(count==n):
            del mylist[i]

print("Updated list: ", mylist)            