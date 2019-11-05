N1 = int(input())
N2 = int(input())
str = 'no'
for i in range(10000):
    if (i >= 0 and i%2 == 0 and i==N1) or (i%2 == 1 and i == N2):
        str = 'yes'
        break
print(str)        
            