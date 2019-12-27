n= int(input())
team = list(list(map(int, input().split(" "))) for k in range(n))

friends = []
team1 = []
team2 = []

for x in range(n):
    friends.append([])
    team[x] = team[x][:-1] 
    for y in range(1, n + 1):
        if y in team[x]:
            friends[x].append(1)
        else:
            friends[x].append(0)

spisok = list(range(1, n+1))

for i in range(n):
    if sum(friends[i]) == 0:
        print(0)
    else:
        for xsort in range(n):
            if spisok[xsort] != 0:
                team1.append(xsort+1)
                spisok[xsort] = 0
                for i in range(xsort, n):
                    if friends[xsort][i] == 1:
                        team2.append(i+1)
                        spisok[i] = 0
print(len(team1))                        
print(*team1)

#for x in range(n):
#    print(*friends[x])