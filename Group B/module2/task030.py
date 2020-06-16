n = int(input())
s = []
for i in range(n + 1):
    for j in range(i):
        s.append(i)
print(*s[:n])
