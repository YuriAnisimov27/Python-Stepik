inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')

sub_1 = []
sub_2 = []
sub_3 = []

for line in inf.readlines():
    student = line.split(';')
    s = 0
    for i in student:
        i = i.strip()
        if i.isdigit():
            s += int(i)
    print(s / 3, file=ouf)
    sub_1.append(int(student[1]))
    sub_2.append(int(student[2]))
    sub_3.append(int(student[3].strip()))

print(sum(sub_1) / len(sub_1), sum(sub_2) / len(sub_2), sum(sub_3) / len(sub_3), file=ouf)

inf.close()
ouf.close()
