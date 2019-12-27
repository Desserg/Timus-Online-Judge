from itertools import chain, dropwhile, repeat

Maska =  []
Text = []

def Maska90(M):
    rotated = tuple(zip(*M[::-1]))
    return rotated

for q in range(4):
    Maska.append(input())
for t in range(4):
    Text.append(input())

s = ''
for x in range(4):
    for mx in range(4):
        for my in range(4):
            if Maska[mx][my] == 'X':
                s += Text[mx][my]
    Maska = Maska90(Maska)       
print(s)
