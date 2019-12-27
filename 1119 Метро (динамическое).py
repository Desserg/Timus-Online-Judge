NM = list(map(int,  input().split(' ')))
n = int(input())

srez = []
srez.append([0, 0]) # добовляем начальную точку графа (граф проходных дворов будет)
for i in range(n):
    srez.append(list(map(int, input().split(' '))))


srez = sorted(srez, key=lambda l: l[0])

srez.append([NM[0] +1, NM[1] +1]) # добавляем конечную точку графа проходных дворов
n += 2

def build_graph():
    G = []
    for j in range(n):
            G.append([])
            vertex(j, G)
    return G
            
def vertex(vr, Gr):
    for ii in range(n):
        if srez[vr][0] < srez[ii][0] and srez[vr][1] < srez[ii][1]: 
            Gr[vr].append(srez[ii])
    return Gr

Graph = build_graph()

path = []
for i in range(n):
    path.append(0)

for i in range(n):
    for item in Graph[i]:
        s = path[i]     # текущий путь
        v = srez.index(item) #индекс элемента из srez
        if path[v] <= s:
            path[v] += 1
        
Max = max(path) - 1

print(round(100*(sum(NM)) - 100*Max*2  + 100*Max*2**0.5))

