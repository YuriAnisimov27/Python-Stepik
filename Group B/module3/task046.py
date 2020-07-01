text, code, text1, code1 = [input() for i in range(4)]
text_dict, code_dict = dict(), dict()
for i in range(len(text)):
    if i not in text_dict:
        text_dict[text[i]] = code[i]
for i in range(len(code)):
    if i not in code_dict:
        code_dict[code[i]] = text[i]
for i in text1:
    print(text_dict[i], end='')
print()
for i in code1:
    print(code_dict[i], end='')
