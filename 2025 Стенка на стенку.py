import sys

def hard(n, k):
    if n%k == 0:
        return n**2*(k-1)//(2*k)
    else:
        k1 = n%k  # команд членов на 1 больше
        k2 = k - k1 
        n2 = n//k * k2 # членов команд на 1 меньше где
        n1 = n - n2
        return hard(n1, k1) + hard(n2, k2) + n1*n2

n = int(input())
members = []
for x in sys.stdin:
    members.append(list(map(int, x.rstrip().split(' '))))
    
for i in range(n):
    print(hard(members[i][0], members[i][1]))


