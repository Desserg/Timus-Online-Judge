n = int(input())
e = list(map(int, input().split(' ')))
door = 0
Max = 0
for i in range(n-2):
    triplet = e[i]+e[i+1]+e[i+2]
    if Max < triplet:
        door = i+2
        Max = triplet
print(Max, door)
    

    