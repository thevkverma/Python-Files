mylist = [15,6,7,8,9,4,1,0,10,10,14,15,9,8,10,4,10,10]
x = 10
count = 0

for ele in mylist:
    if(ele == x):
        count = count + 1

print("{} has occured {} times".format(x,count))
        