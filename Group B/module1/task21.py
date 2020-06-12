n = input()
answer = 'Счастливый' if (int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5])) else 'Обычный'
print(answer)
