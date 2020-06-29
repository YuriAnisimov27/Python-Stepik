import requests

print(requests.get('https://stepic.org/media/attachments/course67/3.6.2/008.txt').text.count('\n'))
