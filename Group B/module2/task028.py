a = sorted(list(map(int, input().split())))
for i in set(a):
    if i in a:
        a.remove(i)
print(*set(a))
