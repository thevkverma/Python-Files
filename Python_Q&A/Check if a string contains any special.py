import re
str = "welcome@@2To%%Python**Programming@!!^%%@$"

regex = re.compile('[@_!#$%^()<>?/\}{~:]')

if(regex.search(str)==None):
    print("No special characters present in a string")

else:
    print("Srting contains special characters")    