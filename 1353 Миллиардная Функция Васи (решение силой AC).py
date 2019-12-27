import math 
#шаг первый: разбиваем число на возможные цифры
def break_number(num):
    #получаем первый наименьший массив из цифр mass
    mass = []
    n9 = num // 9
    n1 = num % 9
    for i in range(9): mass.append(n9)
    for i in range(n1): mass.append(1)
#    else: mass = [1]*num
    #print(mass)
    summ = 0
    while 1:
        #останавливаем когда первый элемен перестает быть цифрой или собрано всего одно число
        if mass[0] == 10: return summ
        elif len(mass) == 1: return summ + combine(mass)
        first = mass[0]
        #берем только те подборки где цифры могут составить 10**9 (по условию задачи не более 9 позиций)
        if len(mass) <= 9:
            #print(mass)
            summ += combine(mass)
            #print(summ)
            #input()
        i = 0
        min_elem = 0
        while i != len(mass) - 1:
            if mass[i] < first:
                first = mass[i]
                min_elem = i
            i += 1
        mass[min_elem] += 1
        mass = mass[:min_elem + 1]
        mass_sum = sum(mass)
        for j in range(0, num - mass_sum):
            mass.append(1)
            
def combine(vec):
    # n!/(n0!*n1!*n2*...n9!)
    x = math.factorial(9)
    fac = vec[0]
    t = 1
    for i in range(1, len(vec)):
        if vec[i] == fac:
            t += 1
            x = x / t
        else:
            fac = vec[i]
            t = 1
    x = x / math.factorial(9 - len(vec)) # n0!
    return x

n = int(input())
if n == 1: print(10)
elif n == 81: print(1)
elif 2 <= n <= 40:
    print(int(break_number(n)))
else: # 40 < n < 81 #этот отрезок зеркален предыдущему, но считается в разы дольше поэтому:
    print(int(break_number(81 - n)))
'''
print('{')
for n in range(82):
    if n == 1: print(10)
    elif n == 81: print(1)
    elif 2 <= n <= 40:
        print(int(break_number(n)),',')
    else: # 40 < n < 81 #этот отрезок зеркален предыдущему, но считается в разы дольше поэтому:
        print(int(break_number(81 - n)),',')
print('}')
'''