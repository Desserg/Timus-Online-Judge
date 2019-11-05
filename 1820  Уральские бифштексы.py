NK = list(map(int, input().split(' ')))
# ((2n+k-1)div k)*m
if NK[0] < NK[1]:
    m = 2  
else:
    m = (2*NK[0] + NK[1] -1)//NK[1]
print(m)