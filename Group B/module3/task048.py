turtle = { 'север': 0, 'запад': 0, 'юг': 0, 'восток': 0 }
for _ in range(int(input())):
    direction, data = input().split()
    turtle[direction] += int(data)
print(turtle['восток'] - turtle['запад'], turtle['север'] - turtle['юг'])
