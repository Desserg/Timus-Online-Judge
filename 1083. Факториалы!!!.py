nk = input().split(' ')

n = int(nk[0])
k = len(nk[1])

if n%k == 0:
    stop = k
else:
    stop = n%k
 
result = 1
for i in range(stop, n+1 , k):
    result *= i
    
print(result)
     

