st = input("Enter Any String: ")

st1 = st.split()
newList = []
for i in st1:
    if len(i)%2==0:
        newList.append((i))
        print(newList)