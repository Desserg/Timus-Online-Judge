n = int(input())

st = list(int(input()) for _ in range(n))

st = sorted(st)

for i in range(n-1, -1, -1):
    print(st[i])

