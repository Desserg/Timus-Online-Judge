n = int(input())
m = []
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append([])
ik = 1
for x in range(0, n):
    i = 0
    j = x
    while j >= 0:
        m[j][i] = ik
        ik += 1
        i +=1
        j -=1
for x in range(1, n):
    i = x
    j = n-1
    while i <= n-1:
        m[j][i] = ik
        ik += 1
        i +=1
        j -=1
for j in range(n):
    if j > 0:
        print()
    for u in range(n-1, -1, -1):
        print(m[u][j], end = ' ')
