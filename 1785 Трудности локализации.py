st = int(input())

d = {'few': range(1,5), 'several': range(5,10), 'pack': range(10,20), 'lots': range(20,50), 'horde': range(50,100), 'throng': range(100,250), 'swarm': range(250,500), 'zounds': range(500,1000), 'legion': range(1000,2001)}

for name, contents in d.items():
    if st in contents:
        print(name)