n = int(input())
spam = []
spisok = []
for i in range(n):
    item = input()
    if (item in spisok) and (spam.count(item) == 0):
        spam.append(item)
    else:
        spisok.append(item)

for item in spam:
    print(item)
        
    
    