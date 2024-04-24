st = "Python is simple and easy language"

st1 = st.split()
v = 'aeiou'
resultList = []
for i in st1:
    if i [0] not in v and i[-1] in v:
        resultList.append(i)

print(resultList)        