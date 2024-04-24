st = input("Enter Any String: ")

st1 = st.split()

for i in st1:
    if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU':
        print(i)