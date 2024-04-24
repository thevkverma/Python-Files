st = 'Python is simple and easy language'
st = st.split()
v = 'aeiou'
resultList = []
for i in st:
    if i[0] in v and i[-1] not in v:
        resultList.append(i)

print(resultList)        