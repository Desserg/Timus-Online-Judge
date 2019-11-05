N = int(input())
guest = 2
for i in range(N):
    str = input()
    guest += 1
    if '+' in str:
        guest +=1
if guest == 13:
    guest += 1
print(guest*100)
        