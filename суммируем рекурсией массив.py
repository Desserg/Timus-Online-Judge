def sumrec(mas):
    sum = 0
    if mas == []:
        return(0)
    else:
        sum = mas[0] + sumrec(mas[1:])
        return(sum)
    
def lenrec(mas):
    lenmas = 0
    if mas == []:
        return(0)
    else:
        lenmas += 1 + lenrec(mas[1:])
        return(lenmas)
    
def maxrec(mas):
    if len(mas) == 1:
        return(mas[0])
    else:
        a = maxrec(mas[1:])
        if mas[0] < a:
            return(a)
        else:
            return(mas[0])
        
def bifindrec(mas, t): # отсортированный массив
    if len(mas) == 1:
        if mas[0] == t:
            return(t)
        else:
            return
    else:
        razrez = len(mas)//2
        if mas[razrez] > t:
            ot = bifindrec(mas[0:razrez], t)
        else:
            ot = bifindrec(mas[razrez:], t)
        return(ot)  
        

test = [1, 6, 3, 5]
test2 = [0, 0, 0]
test3 = [100, 24, 100, 230, 1, 3, 4, 5, 0, 0, -1, 0, 0, 0, 0]

print(sumrec(test), lenrec(test))
print(sumrec(test2), lenrec(test2))
print(sumrec(test3), lenrec(test3))
print('\n', maxrec(test), maxrec(test2), maxrec(test3))
test3.sort()
print(bifindrec(test3, 100))
