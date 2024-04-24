st = input("Enter Any String: ")

st1 = st.split()

for i in st1:
    if i[0] in 'aeiouAEIOU':
           print(i)