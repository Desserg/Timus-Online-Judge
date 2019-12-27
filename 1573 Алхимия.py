b, r, y = map(int, input().split())
n = int(input())
colors = []
for i in range(n):
    colors.append(input()[0])
z = 1
for t in range(n):
    if colors[t] == 'R': z *= r
    elif colors[t] == 'Y': z *= y
    elif colors[t] == 'B': z *= b
print(z)