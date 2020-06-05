import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
counter = 0
parsedxml = xmltodict.parse(xml)
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        name = 'noname'
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    counter += 1
        elif isinstance(tags, dict):
            if (tags['@v']) == 'fuel':
                counter += 1
print(counter)
