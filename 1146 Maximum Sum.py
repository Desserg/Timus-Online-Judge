n = int(input())

q = []

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def printq(matrix):
    for i in range(n):
        print(matrix[i])
    print()

for x in range(n):
    q.append(list(map(int, input().split(' '))))
    
q0 = transpose(q)
q1 = sorted(transpose(q))
               

qx =  [sum(q[i]) for i in range(n)]

printq(q)
printq(q0)
printq(q1)