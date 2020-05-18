from urllib.request import urlopen

html = urlopen("file:///Users/urij/Downloads/1.html").read()
s = str(html)
countPython = s.count('Python')
countC = s.count('C++')
print(countPython, countC)
