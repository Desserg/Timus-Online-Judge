from struct import *
import sys

team2 = []
j = 0
for line in sys.stdin:
    if j == 0:
        n = int(line.rstrip('\n'))
    else:
        strtemp = line.rstrip('\n')
        team2.append(strtemp.split(' '))
        team2[j-1][1] = int(team2[j-1][1])
        #team2[j-1][0] = pack('I', int(team2[j-1][0])) # запаковываем int в 4 байта
        #team2[j-1][1] = pack('B', int(team2[j-1][1])) # запаковываем int в один байт
    j += 1
    
for j in range(n-1):
    f = 0
    for i in range(n-j-1):
        if team2[i][1] < team2[i+1][1]:
            team2[i], team2[i+1] = team2[i+1], team2[i]
            f = 1
    if f == 0:
        break
    
for i in range(n):
#    print(*unpack('I', team2[i][0]), *unpack('B', team2[i][1]))
    print(team2[i][0], team2[i][1])
