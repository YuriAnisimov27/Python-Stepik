from urllib.request import urlopen
import re

html = urlopen("file:///Users/urij/Downloads/2.html").read()
s = str(html)
regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, s))
myDict = dict()
for i in l:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
myArray = []
for i in myDict:
    myArray.append([myDict[i], i])


def makeTuple(man):
    return (-man[0], man[1])


myArray.sort(key=makeTuple)
firstEl = myArray[0][1]

if myArray[0][0] == myArray[1][0]:
    counter = 1
    print(firstEl, end=' ')
    while myArray[0][0] == myArray[counter][0]:
        print(myArray[counter][1], end=' ')
        counter += 1
else:
    print(firstEl)
