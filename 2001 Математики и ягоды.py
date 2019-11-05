ab1 = list(map(int, input().split(' ')))
ab2 = list(map(int, input().split(' ')))
ab3 = list(map(int, input().split(' ')))
x = [ab1[0] - ab3[0], ab1[1] - ab2[1]]
print(x[0], x[1])