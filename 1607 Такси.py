AbCd = list(map(int, input().split(' ')))

balance = (AbCd[2] - AbCd[0]) % (AbCd[1] + AbCd[3])

n = (AbCd[2] - AbCd[0]) // (AbCd[1] + AbCd[3])

if AbCd[0] > AbCd[2]:
    print(AbCd[0])
elif balance < AbCd[1]:
    print(AbCd[2] - n*AbCd[3])
else:
    print(AbCd[0] + n*AbCd[1] + AbCd[1])