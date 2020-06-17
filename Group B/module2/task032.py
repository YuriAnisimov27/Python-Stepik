line = input()
matrix = []
while line != 'end':
    matrix.append(list(map(int, line.split())))
    line = input()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        item = matrix[i - 1][j] + matrix[(i + 1) % len(matrix)][j] + matrix[i][j - 1] + matrix[i][
            (j + 1) % len(matrix[i])]
        print(item, end=' ')
    print()
