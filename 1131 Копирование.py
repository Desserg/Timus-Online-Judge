import math

nk = list(map(int, input().split(' ')))
n = nk[0] 
k = nk[1]

if n > 1:
    t = int(math.log2(k)) + 1
    a = 2**t
    if n > a:
       t = t + (n - a)//k if (n - a)%k == 0 else t + (n - a)//k + 1
    elif n <= a:
        temp = math.log2(n)
        t = int(temp) if float.is_integer(math.log2(n)) else int(temp) + 1
else:
    t = 0
    
print(t)