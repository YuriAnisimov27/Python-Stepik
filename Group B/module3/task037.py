n = int(input())
d = {}
for i in range(1, n + 1):
    a = int(input())
    if a in d:
        print(d[a])
    else:
        d[a] = f(a)
        print(f(a))
