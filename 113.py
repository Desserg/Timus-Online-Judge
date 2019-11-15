import sys

team = []
team = sys.stdin.readlines()
n = int(team[0].rstrip())
del team[0]

for i in range(n):
    strtemp = team[i].rstrip() 
    team[i] = strtemp.split(' ')

for i in range(n):
    team[i][1] = int(team[i][1])
    
team.sort(key = lambda i: i[1], reverse=True)

for i in range(n):
    print(*team[i])
