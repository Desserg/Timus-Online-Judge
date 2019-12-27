import sys
import math

def pr(nn):
    x1 , y1 = map(float, input().split())
    xs, ys = x1, y1
    xy = []
    P = 0
    for x in range(nn-1):
         st = sys.stdin.readline()
         xt, yt = map(float, st.split())
         P += math.hypot(xt - x1, yt - y1)
         x1, y1 = xt, yt
    P += math.hypot(xt - xs, yt - ys)
    return P

n, r = map(float, input().split())
if n > 1:
    Perim = pr(int(n)) + 2 * math.pi * r
else:
    Perim = 2 * math.pi * r
print(round(Perim,2))