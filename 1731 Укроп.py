nm = list(map(int, input().split()))

print(*[i for i in range(1, nm[0]+1)])
print(*[i for i in range(101, (nm[1])*50 + 101, 50)])
