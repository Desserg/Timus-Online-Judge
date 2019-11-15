import sys

parambook = []
parambook = list(map(int, input().split(' ')))

stroki = parambook[0]
sumbol = parambook[1]
n = parambook[2]

lenwords = []

for i in range(n):
    lenwords.append(len(input()))
    
stranica = 1
current_stroki = stroki

while len(lenwords) > 0:
    
    while current_stroki > 0:
        current_sumbol = sumbol
        while current_sumbol > 0:
            current_sumbol -= lenwords.pop(0)
            if current_sumbol > 0:
                current_sumbol -= 1 # добавляем пробел
            if len(lenwords) == 0:
                current_sumbol = 0
                current_stroki = 0
        current_stroki -= 1   
    stranica += 1
    
print(stranica)