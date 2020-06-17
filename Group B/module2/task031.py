lst = list(map(int, input().split()))
x = int(input())

if x not in lst:
    print('Отсутствует')
for i in lst:
    if i == x:
        print(lst.index(i), end=' ')
        lst[lst.index(i)] += 1
