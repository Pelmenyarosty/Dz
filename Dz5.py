# -*- coding: utf-8 -*-
"""untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Pelmenyarosty/a93c8b3838af7cde855ca3650197d850/untitled9.ipynb
"""

# Задача 1
k = int(input())
u = set()
for i in range(k):
   a = input()
   u.add(a)
print(len(u))

# Задача 2
# делал без учета пробелов после знаков
s = input()
q = s[0].upper()
s = q + s[1:]
s = list(s)
s.append(" ")
c = 0
while True:
    n = s[c:]
    if "." not in n:
        break
    else:
     a = s.index(".", c)
     k = a + 1
     g = s[k].upper()
     s[k] = g
     c += (a + 1)
c = 0
while True:
    n = s[c:]
    if "!" not in n:
        break
    else:
     a = s.index("!", c)
     k = a + 1
     g = s[k].upper()
     s[k] = g
     c += (a + 1)
c = 0
while True:
    n = s[c:]
    if "?" not in n:
        break
    else:
     a = s.index("?", c)
     k = a + 1
     g = s[k].upper()
     s[k] = g
     c += (a + 1)
print("".join(s))

#задача 3
q = input()
w = input()
q = q.replace(" ","")
w = w.replace(" ","")
q = set(q)
w = set(w)
if q == w:
   print("Эти строки - анаграммы")
else:
    print("Эти строки не являются анаграммами")

# Задача 4
q = input()
w = input()
e = input()
q = set(q.split())
w = set(w.split())
e = set(e.split())
w = w.intersection(q)
e = list(e.intersection(w))
e = list(sorted(e))
if len(e) > 0:
   print( "Все три задачи решил(и) - ", ", ".join(e))
else:
    print( "Все три задачи никто не решил")
