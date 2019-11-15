N = int(input())
m = []
for i in range(N):
    l = list(map(int, input().split(' ')))
    m.append(l)
    
e = []
for x in range(0, N):
    i = 0
    j = x
    while j >= 0:
        e.append(m[j][i])
        i +=1
        j -=1
for x in range(1, N):
    i = x
    j = N-1
    while i <= N-1:
        e.append(m[j][i])
        i +=1
        j -=1
for x in e:
    print(x, end = ' ')        

    