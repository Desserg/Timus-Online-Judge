lr = list(map(int, input().split(' ')))

v1 = lr[1]*2 + 40
v2 = 39*2 + 40 + 2*(lr[0]-40) + 1
if v1 > v2:
    print(v1)
else:
    print(v2)