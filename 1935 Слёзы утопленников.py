n = int(input())

a = list(map(int, input().split(' ')))

a.sort()
result = a[n-1]
for i in range(n):
    result += a[i]
print(result)    
    