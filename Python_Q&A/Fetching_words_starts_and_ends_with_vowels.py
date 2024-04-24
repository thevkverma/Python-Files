st = input("Enter Any String: ")

st1 = st.split()

for i in st1:
    if i[0] and i[-1] in 'aeiouAEIOU':
        print(i)