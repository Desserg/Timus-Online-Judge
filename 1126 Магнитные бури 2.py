import sys
import random
m = int(input())
b = []
c = []
a = []

a.pop()

b.append(a[0])
# Расчитываем B
for i in range(1,len(a)):     
    if i % m:
        b.append(max(a[i], b[i - 1]))
    else:
        b.append(a[i])
# Расчитываем C
c.append(a[-1])
for i in range(len(a) - 1, -1, -1):
    if (i + 1) % m:
        c.append(max(a[i], c[len(a) - i - 1]))
    else:
        c.append(a[i])
c = c[::-1]
z = ''
for i in range(0, len(a)-m + 1):
    z += str(max(c[i], b[i+m-1])) + '\n'
sys.stdout.write(z)
sys.stdout.flush()