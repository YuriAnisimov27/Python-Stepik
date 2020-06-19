def modify_list(l):
    # for i in l:
    #     if i % 2 != 0:
    #         l.remove(i)
    l = list(map(lambda x: x // 2, l))


lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
