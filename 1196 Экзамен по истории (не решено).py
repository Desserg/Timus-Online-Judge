import sys

nprof = int(sys.stdin.readline())
prof = []
stud = []

for i in range(nprof):
    prof.append(sys.stdin.readline())
    
nstud = int(sys.stdin.readline())

for i in range(nstud):
    stud.append(sys.stdin.readline())

profstud = set(prof) & set(stud)

print(len(profstud))
