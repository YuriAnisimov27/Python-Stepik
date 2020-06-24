with open('input.txt') as inf:
    s = inf.readline().strip()
ouf = open('output.txt', 'w')

symb = s[0]
counter = 0
for i in range(1, len(s)):
    if s[i].isalpha():
        print(symb * counter, end='', file=ouf)
        counter = 0
        symb = s[i]
    if s[i].isdigit():
        counter = counter * (10 ** len(str(counter))) + int(s[i])
    if i == len(s) - 1:
        print(symb * counter, end='', file=ouf)

ouf.close()
