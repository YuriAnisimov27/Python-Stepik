#!/usr/bin/env python3
fout = open('index.html', 'w', encoding='utf8')

print("Content-type: text/html")

print("<html>", file=fout)
print("<body>", file=fout)
print("<table>", file=fout)
for i in range(1, 11):
    print("<tr>", file=fout)
    for j in range(1, 11):
        print("<td>", i * j, "</td>", file=fout)
    print("</tr>", file=fout)
print("</table>", file=fout)
print("</body>", file=fout)
print("</html>", file=fout)

fout.close()
