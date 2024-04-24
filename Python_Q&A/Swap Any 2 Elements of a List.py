mylist = [23,65,19,90]
print(mylist)

pos1, pos2 = 1,3

mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]
print(mylist)