#работает но медленно 1.8 - 1.9 секунды (на тимусе тест не проходит >2 сек)
from collections import deque
import time
import sys

def main():
    #nab =  list(map(int, readsys.split()))
    for x in sys.stdin:
        nab = list(map(int, x.rstrip().split(' ')))
    start_time = time.time()
    a = min(nab[1], nab[2])
    b = max(nab[1], nab[2])
    sta, stb = L(a, b)
    sta = deque(sta, len(sta))
    stb = deque(stb, len(stb))
    for x in range(nab[0]-a):
        sta, stb = stateL(sta, stb)
    print((sum(sta) + sum(stb)) % 1000000007)
    print("--- %s seconds ---" % (time.time() - start_time))  

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

