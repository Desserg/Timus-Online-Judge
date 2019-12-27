from collections import deque
import sys

def main():
    for x in sys.stdin:
        nab = list(map(int, x.rstrip().split(' ')))
    a = min(nab[1], nab[2])
    b = max(nab[1], nab[2])
    sta, stb = L(a, b)
    sta = deque(sta, len(sta))
    stb = deque(stb, len(stb))
    for x in range(nab[0]-a):
        sta, stb = stateL(sta, stb)
    print((sum(sta) + sum(stb)) % 1000000007)

def stateL(ma, mb):
    suma = sum(mb) % (1000000007)
    sumb = sum(ma)  % (1000000007)
    ma.appendleft(suma)
    mb.appendleft(sumb)
    return ma, mb

def L(a, b):
    la = []
    for i in range(a-2,-1,-1):
        la.append(2**i)
    la.append(1)
    lb = la[:]
    for i in range(b-a):
        lb.append(0)
    return la, lb

main()

