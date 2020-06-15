a = list(map(int, input().split()))
if len(a) == 1:
    print(*a)
else:
    for i in range(len(a)):
        print(a[i - 1] + a[(i + 1) % len(a)], end=' ')
