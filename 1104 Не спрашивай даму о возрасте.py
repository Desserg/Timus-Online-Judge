import sys
string = sys.stdin.read()
age = string[:-1]
min_b = 1

number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
def num_basis(stroka):
    global min_b
    num = 0
    for x in stroka:
        a = number[x]
        num += a
        if a > min_b:
            min_b = a
    return num

def num_find(x, b):
    if x % (b - 1) == 0:
        return b
    else:
        return 'No solution.'
num_age = num_basis(age)

for i in range(min_b+1, 37):
    temp = num_find(num_age, i)
    if temp != 'No solution.':
        break
print(temp)



