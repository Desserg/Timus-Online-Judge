import sys

def f():
    prep = set(input() for _ in range(int(input())))
    input()
#    print(sum(i in prep for i in map(str.rstrip, sys.stdin)))
 
f()