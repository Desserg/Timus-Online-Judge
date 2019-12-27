n = int(input())
team = list(input().split(' ') for _ in range(n))

sortstr = {}
sortteam2 = {}
str0 = "Isenbaev"


def foo(chelik, c, spisok):
    spisok2 = []
    sortstr[chelik] = sortteam[chelik]
    for team in spisok:
        if chelik in team:
            for x in range(3):
                if (team[x] in sortteam) == False:
                    sortteam2[team[x]] = c + 1
        else:
            spisok2.append(team)
    return spisok2

def start():
    global sortteam, team
    sortteam = {str0 : 0}
    while sortteam != {}:
        for key, value in sortteam.items():
            team = foo(key, value, team)
        sortteam = sortteam2.copy()
        sortteam2.clear()
    team = sum(team, [])

    for i in team:
        sortstr[i] = 'undefined'

    for key in sorted(sortstr.keys()):
        print(key, sortstr[key])
        
def noIsenbaev():
    global team
    team = sum(team, [])
    for i in team:
        sortstr[i] = 'undefined'
    for key in sorted(team):
        print(key, sortstr[key])

flag = 0
for i in team:
    if "Isenbaev" in i:
        flag = 1        
        break
if flag == 1:    
    start()
else:
    noIsenbaev()
        
