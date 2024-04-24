mylist = [1,6,3,5,3,4]
ele = 4
flage = 0

for i in mylist:
    if(i==ele):
        print("Element found")
        flage =1
        break
if(flage==0):
    print("Element Not Found")    