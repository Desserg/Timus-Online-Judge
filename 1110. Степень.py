a = list(map(int, input().split(' ')))
N = a[0]
M = a[1]
Y = a[2]

x = []
if M <= Y:
    x.append(-1)
else:
    for i in range(M):
        if (i**N) % M == Y:
            x.append(i)
    if len(x) == 0:
        x.append(-1)
print(*x)