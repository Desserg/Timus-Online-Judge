a = int(input())
b = int(input())

if a == b and a%2 == 0:
    print(0)
elif a == b and a%2 != 0:
    print(1)
else:
    if a%2 or b%2:
        print((b-a)//2+1)
    else:
        print(int((b-a)/2))