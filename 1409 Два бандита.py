d = input().split(' ')
for i, item in enumerate(d):
    d[i] = int(item)-1  
print(d[1], d[0])