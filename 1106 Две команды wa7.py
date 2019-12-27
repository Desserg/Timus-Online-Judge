team = list([k+1] + list(map(int, input().split(" "))) for k in range(int(input())))

team = sorted(team, key=len)
#print(team)
subteam = []
subteam2 = []

def sort(fr):
    f = 0
    if 0 in fr:
        fr.remove(0)
        
        
    for x in fr:
        if f == 1 and (x not in subteam2):
            subteam2.append(x)
        elif (x not in subteam) and (x not in subteam2):
            subteam.append(x)
            f = 1   
        
for friends in team:
    zeroteam = 0
    if max(friends[1:]) == 0:
        print(0)
        zeroteam = 1
        break
    else:
        sort(friends)

if zeroteam == 0:
    subteam = sorted(subteam)
    print(len(subteam))
    print(*subteam)
else:
    print('???')