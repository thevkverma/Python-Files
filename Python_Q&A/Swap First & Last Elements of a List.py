mylist = [12,35,9,58,71,45]
size = len(mylist)

temp = mylist[0]
mylist[0] = mylist[size-1]
mylist[size-1]=temp

print("list after swapping: ",mylist)