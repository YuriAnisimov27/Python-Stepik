import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
counterIn, counterNotIn = 0, 0
parsedxml = xmltodict.parse(xml)
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        counterIn += 1
    else:
        counterNotIn += 1
print(counterIn, counterNotIn)
