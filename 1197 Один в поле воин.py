sumb = {'a': 4, 'b': 3, 'c': 2, 'd':1, 'e': 1, 'f': 2, 'g': 3, 'h': 4}
num = {'1': 4, '2': 3, '3': 2, '4':1, '5':1, '6':2, '7': 3, '8': 4}
fild = {11: 8, 12: 8, 13: 6, 14: 4, 22: 8, 23: 6, 24: 4, 33: 4, 34: 3, 44: 2}
n= int(input())
H = []
for i in range(n):
    x = list(input())
    ax = sumb[x[0]]
    ay = num[x[1]]
    if ax > ay:
        ax, ay = ay, ax
    H.append(fild[ax*10+ay])

for i in H:
    print(i)