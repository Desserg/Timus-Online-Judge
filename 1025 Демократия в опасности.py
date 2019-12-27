n = int(input())
party = list(map(int, input().split(' ')))

nspis = n//2 + 1

party.sort()
golosa = 0

for i in range(nspis):
    golosa += party[i]//2 + 1

print(golosa)