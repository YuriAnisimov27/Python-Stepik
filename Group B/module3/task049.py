classes = {
    'class1': 0,
    'students1': 0,
    'class2': 0,
    'students2': 0,
    'class3': 0,
    'students3': 0,
    'class4': 0,
    'students4': 0,
    'class5': 0,
    'students5': 0,
    'class6': 0,
    'students6': 0,
    'class7': 0,
    'students7': 0,
    'class8': 0,
    'students8': 0,
    'class9': 0,
    'students9': 0,
    'class10': 0,
    'students10': 0,
    'class11': 0,
    'students11': 0
}

with open('input.txt', encoding='UTF8') as inf:
    for line in inf:
        line = line.strip()
        if line != '':
            data = line.split('\t')
            classes['class%s' % int(data[0])] += int(data[2])
            classes['students%s' % int(data[0])] += 1

ouf = open('output.txt', 'w')
for i in range(1, 12):
    if classes['students%s' % i] == 0:
        print(i, '-', file=ouf)
    else:
        print(i, classes['class%s' % i] / classes['students%s' % i], file=ouf)
ouf.close()
