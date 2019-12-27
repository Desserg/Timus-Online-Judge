import sys

def f():
    n = int(input())
    s = list(map(int, input().split(" ")))
    a = sum(s)/n
    print('%.6f' % a)
f()