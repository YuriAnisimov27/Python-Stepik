def zm(m, n):
    dx, dy = 0, 1
    x, y = 0, 0
    arr = [[None] * m for _ in range(n)]
    for i in range(1, n * m + 1):
        arr[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy
    for i in arr:
        for j in i:
            print(j, end=' ')
        print(' ')


n = int(input())
zm(n, n)
