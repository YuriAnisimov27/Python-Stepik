from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("file:///Users/urij/Downloads/5.html").read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
answer = 0

for a in soup.find_all('td'):
    answer += int(a.get_text())
print(answer)
