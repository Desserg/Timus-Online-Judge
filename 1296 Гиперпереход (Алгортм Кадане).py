import sys

def Kadane(a):
    ans = a[0]
    sum_r = 0
    min_sum = 0;
    for r in range(n):
        sum_r +=a[r]
        ans = max(ans, sum_r - min_sum)
        min_sum = min(min_sum, sum_r)
    if ans <= 0:
        return 0
    else:
        return ans

n = int(input())
if n == 0:
    print(0)
else:
    emc =  list(int(i) for i in map(str.rstrip, sys.stdin))    
    print(Kadane(emc))


    
