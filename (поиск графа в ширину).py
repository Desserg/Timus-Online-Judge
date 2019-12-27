from collections import deque
import sys

NM = list(map(int,  input().split(' ')))
n = int(input())
#srez = list(i for i in map(str.rstrip, sys.stdin))

srez = [] 
for i in range(n):
    srez.append(list(map(int, input().split(' '))))

fin = [NM]
graph = {}



search_queue = deque() #создание очереди
search_queue += graph(start) #добавляем соседние точки в очередь
search(start)

def create_graph(fin, srez):

   


def station_is_fin(x):
    return x == fin

def search(x):
    search_queue = deque()
    search_queue += graph[x]
    searched = [] # этот массив используется для отслеживания уже проверненных пунктов
    while search_queue:
        station = search_queue.popleft()
        if not person in searched: # пункт проверяется только в том случае если не был проверен ранее
            if person_is_fin(station):
                return True
            else:
                search_queue += graph[station]
                searched.append(station) # пункт помечается как проверенный
    return False

'''
while search_queue: # пока очередь не пуста
    station = search_queue.popleft() #  очереди извлекается первый пункт
    if station_is_fin(station): # Проверяем, не последний ли пункт
        return True
    else:
        search_queue += rgaph[station]  #Нет не является. Все соседнии пункты добавляются в очередб поиска
return False # Если выполнение дошло доэтой строки, значит в очереди нет конечного пункта
'''