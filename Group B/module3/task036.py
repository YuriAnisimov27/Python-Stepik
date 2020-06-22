d = dict()
for i in input().split():
    d[i.lower()] = d[i.lower()] + 1 if i.lower() in d else 1

for key, value in d.items():
    print(key, value)
