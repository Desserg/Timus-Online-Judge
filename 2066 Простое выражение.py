M = [int(input()), int(input()), int(input())]
M.sort()
print(min(M[0]-M[1]-M[2],M[0]-M[1]*M[2]))
