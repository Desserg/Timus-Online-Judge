qz = list(map(int, input().split(' ')))

t = sum(list(map(int, input().split(' ')))) * 20

if qz[1] - t >= qz[0]:
    print("No chance.")
else:
    print("Dirty debug :(")


