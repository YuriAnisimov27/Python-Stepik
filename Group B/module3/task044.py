import requests

index = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
url = 'https://stepic.org/media/attachments/course67/3.6.3/'

while index[0:2] != "We":
    index = requests.get(url + index).text
print(index)
