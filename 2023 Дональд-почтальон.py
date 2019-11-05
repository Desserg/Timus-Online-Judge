sh = {0: {'A', 'P', 'O', 'R'}, 1: {'B', 'M', 'S'}, 2: {'D', 'G','J', 'K', 'T', 'W'}}
n = int(input())
d = 0
shag = 0
for i in range(n):
    s = input()
    for name, contents in sh.items():
        if s[0] in contents:
            h = name
            shag += abs(h - d)
            d = h
print(shag)
        
    