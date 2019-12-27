import sys

def f():
    prep = set(input() for _ in range(int(input())))
    input()
    print(sum(i in prep for i in map(str.rstrip, sys.stdin)))
 
f()
'''
то что выше развернуто
import sys
 
def f():
    prep = set()
    pn = int(input())
    while pn > 0:
        prep.add(input())
        pn -= 1
    input()
    n = 0
    for i in map(str.rstrip, sys.stdin):
        if i in prep:
            n += 1
    print(n)
 
f()

'''
'''
nprof = int(sys.stdin.readline())
prof = []
stud = []
n= 0 # овпадений дат студента и проффесора

for i in range(nprof):
    prof.append(sys.stdin.readline())
    
nstud = int(sys.stdin.readline())

for i in range(nstud):
    stud.append(sys.stdin.readline())

for i in stud:
    if i in prof:
        n += 1
print(n)
'''