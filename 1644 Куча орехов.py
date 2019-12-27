import sys

n = int(input())

experiens =  list(i.split(' ') for i in map(str.rstrip, sys.stdin))

M = 10
m = 2
for i in range(n):
    if experiens[i][1] == 'hungry':
        m = max(m, int(experiens[i][0]))
    else:
        M = min(M, int(experiens[i][0]))
if M > m:
    print(M)
else:
    print('Inconsistent')
