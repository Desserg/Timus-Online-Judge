import sys
import collections

polz = list(input() for _ in range(int(input())))
#print(polz)
result = {i: polz.count(i) for i in polz}

s = 0
for key, i in result.items():
    if result[key] >= 4:
        s += result[key]//4
print(s)