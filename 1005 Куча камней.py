# Считываем данные
N = int(input())
weight = list(map(int, input().split(' ')))
# weight = sorted(weight)
# weight.reverse()            # Список камней по возрастанию

'''
Задача разбиения множества чисел
https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0_%D1%87%D0%B8%D1%81%D0%B5%D0%BB
'''
# Создаем массив P
S = [0] + weight
K = sum(S)
X = K//2+1
Y = len(S)+1
P = []

for i in range(X):
    P.append([])
    for j in range(Y):
        if i == 0:
            P[i].append(True)
        else:
            P[i].append(False)        

for i in range(1, X):
    for j in range(1, Y):
        if (i - S[j-1]) >= 0:
            P[i][j] = (P[i][j-1] or P[i - S[j-1]][j-1])
        else:
            P[i][j] = (P[i][j-1])

#print(str(P[K//2]))
#Находим иальный вес
for i in range(X-1, -1, -1):
    if True in P[i]:
        print(K - 2*i)
        break
       

for i in range(0, (K//2+1)):
    print(str(i) + str(P[i]) + '\n')
        