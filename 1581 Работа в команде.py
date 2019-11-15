n = int(input())
data = list(map(int, input().split(' ')))

cipherstr = []

def cipher(c, t):
    cipherstr.append(c)
    cipherstr.append(t)

count = 1
tnum = data[0]
for i in range(1, n):
    if tnum == data[i]:
        count += 1
    else:
        cipher(count, tnum)
        tnum = data[i]
        count = 1
cipher(count, tnum)
for i in cipherstr:
    print(i, end= ' ')