n1 = int(input())
N1 = list(map(int, input().split(' ')))
n2 = int(input())
N2 = list(map(int, input().split(' ')))
n3 = int(input())
N3 = list(map(int, input().split(' ')))
print(len(set(N1)&set(N2)&set(N3)))

