import sys

def inp():
    team = list(input().split(' ') for _ in range(int(input()))) 
    team.sort(key = lambda i: int(i[1]), reverse=True)
    return team

t = inp()
for i in t:
    print(*i)
