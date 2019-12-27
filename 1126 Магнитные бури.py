import sys
from collections import deque

m = int(input())
ms = []
sensors = deque([],m)
z = ''
max_el = 0
it = 0
for i, x in enumerate(sys.stdin):
    s = int(x.rstrip())
    sensors.appendleft(s)
    if s > max_el:
        max_el = s
        it = m
    it -= 1
    if it == 0:
        max_el = max(sensors)
        it = m - sensors.index(max_el)
    if i >= m-1 and s >= 0:
        z += str(max_el) + '\n'    
sys.stdout.write(z)
sys.stdout.flush()



