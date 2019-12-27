data = list(map(int, input().split(' ')))

tt = data[0]
to = data[1] * 2
t1 = data[2]
t2 = data[3]

if t1 == t2:
    print(tt)
elif t2 - t1 < 0:
    print((t1 - t2)*(tt + to) + tt)
else:
    print(to + (t2 - t1 - 1)*(tt + to))