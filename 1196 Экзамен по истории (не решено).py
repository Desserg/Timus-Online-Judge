import sys

def f():
    prep = set(input() for _ in range(int(input())))
    input()
    print(sum(i in prep for i in map(str.rstrip, sys.stdin)))
 
f()

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