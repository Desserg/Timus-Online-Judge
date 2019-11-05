import fileinput

total = []

for line in fileinput.input():   # читает строку после строки, пока нет Ctrl+D
    lst = line.split()           # lst будет списком отдельных чисел, но как строк
    numbers = map(int, lst)      # применит функцию int к всякому элементу списка lst
    total.extend(numbers)        

for i in total[::-1]:
    A = round(i**0.5, 4)
    print("%.4f" %A)