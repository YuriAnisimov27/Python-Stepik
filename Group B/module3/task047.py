words_count = int(input())
words = set([input().lower() for i in range(words_count)])

mistakes = set()
lines_to_test = int(input())
for i in range(lines_to_test):
    line = input()
    for word in line.split():
        if word.lower() not in words:
            mistakes.add(word.lower())

for word in mistakes:
    print(word)
