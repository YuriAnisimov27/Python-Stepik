a, b, x, y = (int(input()) for x in range(4))

for k in range(x, y + 1):
    print(' ', k, end='')
print()
for i in range(a, b + 1):
    print(i, end=' ')
    for j in range(x, y + 1):
        print(i * j, end=' ')
    print()
