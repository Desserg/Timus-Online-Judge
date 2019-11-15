n = list(input())

if len(n) == 2:
    n[0] = int(n[0])
else:
    n[0] = int(n[0])*10 + int(n[1])
    n.pop(1)

if n[1] == 'A' or (n[1] == 'F') and (n[0] in range(3,21)) or n == [1, 'D'] or n == [2, 'D'] or n[1] == 'K':
    print("window")
elif n[0] < 21:
    print("aisle")
elif n[1] == 'B' or n[1] == 'E' or n[1] == 'F' or n[1] == 'J':
    print("neither")
else:
    print("aisle")
    
