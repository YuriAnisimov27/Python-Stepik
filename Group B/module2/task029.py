n = int(input())
s = n
answer = n ** 2
while s:
    n = int(input())
    s += n
    answer += n ** 2
print(answer)
