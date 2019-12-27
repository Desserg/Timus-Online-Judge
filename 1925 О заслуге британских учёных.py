import sys

na = list(map(int, input().split(' ')))
tra = []
for i in range(na[0]):
   tra.append(list(map(int, sys.stdin.readline().split(' '))))
   
Sum = sum(map(lambda x: x[0], tra)) + na[1]
Sum2 = sum(map(lambda x: x[1], tra))

a = Sum - Sum2 - 2*(na[0] + 1)

if a >= 1:
    print(a)
else:
    print("Big Bang!")




