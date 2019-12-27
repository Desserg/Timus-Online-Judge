import collections, math

n = int(input())
c = collections.Counter(input().split(' '))

n1 = c['1']
n2 = c['2']
n3 = c['3']

P = math.factorial(n1+n2+n3)/math.factorial(n1)/math.factorial(n2)/math.factorial(n3)

if P >= 6:
    print('Yes')
else:
    print('No')