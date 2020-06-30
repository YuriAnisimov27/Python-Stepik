scores = dict()
n = int(input())
for _ in range(n):
    s = input()
    if s.split(';')[0] not in scores:
        scores[s.split(';')[0]] = {'games': 0, 'wins': 0, 'draw': 0, 'loses': 0}
    if s.split(';')[2] not in scores:
        scores[s.split(';')[2]] = {'games': 0, 'wins': 0, 'draw': 0, 'loses': 0}
    if int(s.split(';')[1]) < int(s.split(';')[3]):
        scores[s.split(';')[0]]['games'] += 1
        scores[s.split(';')[2]]['games'] += 1
        scores[s.split(';')[0]]['loses'] += 1
        scores[s.split(';')[2]]['wins'] += 1
    elif int(s.split(';')[1]) > int(s.split(';')[3]):
        scores[s.split(';')[0]]['games'] += 1
        scores[s.split(';')[2]]['games'] += 1
        scores[s.split(';')[2]]['loses'] += 1
        scores[s.split(';')[0]]['wins'] += 1
    else:
        scores[s.split(';')[0]]['games'] += 1
        scores[s.split(';')[2]]['games'] += 1
        scores[s.split(';')[2]]['draw'] += 1
        scores[s.split(';')[0]]['draw'] += 1
for i in scores:
    print(i, ':', sep='', end='')
    print(*scores[i].values(), end=' ')
    print(int(scores[i]['wins']) * 3 + int(scores[i]['draw']))
