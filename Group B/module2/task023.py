a, b = int(input()), int(input())
mul = a * b
while mul >= max(a, b):
    if mul % a == mul % b == 0:
        answer = mul
    mul -= 1
print(answer)
