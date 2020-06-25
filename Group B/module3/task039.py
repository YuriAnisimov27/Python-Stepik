inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')

answer = dict()
for line in inf.readlines():
    for i in line.split():
        i = i.lower()
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1

max_value = max(answer.values())
final_dict = {k: v for k, v in answer.items() if v == max_value}

my_list = []
for i in final_dict:
    my_list.append(i)
my_list.sort()

print(my_list[0], final_dict[my_list[0]], file=ouf)
inf.close()
ouf.close()
