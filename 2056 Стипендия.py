n = int(input())

grade = []
G5 = set([5])
G3 = set([3])
for i in range(n):
    grade.append(int(input()))
    
setgrade = set(grade)
if G5 == setgrade:
    print("Named")
elif G3 & setgrade:
    print("None")
else:
    average_grade = sum(grade)/len(grade)
    if average_grade >= 4.5:
        print("High")
    else:
        print("Common")
    
    