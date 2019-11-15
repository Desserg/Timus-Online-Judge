import sys

weight = []

weight = sys.stdin.readlines()
#weight = ['5\n', '5 8 13 27 14\n']
N = int(weight[0].rstrip())
del weight[0]

weight = weight[0].rstrip()
weight = list(map(int, weight.split(' ')))

S = [0] + weight
K = sum(S)
X = K//2+1
Y = len(S)

def dinamicproc(dP):
    for i in range(0, X):
        dP.append([])
        for j in range(0, Y):
            if i == 0:
                dP[i].append(True)
            elif j == 0:
                dP[i].append(False)
            else:    
                if (i - S[j-1]) >= 0:
                    dP[i].append(dP[i][j-1] or dP[i - S[j-1]][j-1])
                else:
                    dP[i].append((dP[i][j-1]))
    return(dP)                

#print(str(P[K//2]))
#Находим иальный вес
def ideal(iP):
    for i in range(X-1, -1, -1):
        if True in iP[i]:
            return(K - 2*i)
            break
    return

M = max(S)
if M >= X:
    print(M - (K - M))
else:
    P = []
    P = dinamicproc(P)
    print(ideal(P))

#for i in range(0, (K//2+1)):
#   print(str(i) + str(P[i]) + '\n')
        
