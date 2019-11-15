from struct import *
import sys
'''
#team = {}
#team = sys.stdin.readlines()
team = ['8\n', '1 2\n', '16 3\n', '11 2\n', '20 3\n', '3 5\n', '26 4\n', '7 1\n', '22 4\n']
n = int(team[0].rstrip())
del team[0]
for i in range(n):
    strtemp = team[i].rstrip() 
    team[i] = strtemp.split(' ')

'''
team = []
n = int(input())

for i in range(n):
    team.append(input().split())
    team[i][0] = int(team[i][0])
    team[i][0] = pack('I', int(team[i][0])) # запаковываем int в 4 байта
    team[i][1] = int(team[i][1])
    team[i][1] = pack('B', int(team[i][1])) # запаковываем int в один байт
    
team.sort(key = lambda i: i[1], reverse=True)


for i in range(n):
    print(*unpack('I', team[i][0]), *unpack('B', team[i][1]))
    