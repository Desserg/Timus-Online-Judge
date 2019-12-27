M = []

for i in range(5):
    M.append(list(map(int, input().split(' '))))

sindex = ['1 2 3 4 5', '1 3 2 4 5', '1 4 3 2 5', '1 3 4 2 5']
s = []
s.append(M[0][1] + M[1][2] + M[2][3] + M[3][4])
s.append(M[0][2] + M[2][1] + M[1][3] + M[3][4])
s.append(M[0][3] + M[3][2] + M[2][1] + M[1][4])
s.append(M[0][2] + M[2][3] + M[3][1] + M[1][4])

mins = min(s)

print(min(s))
print(sindex[s.index(mins)])