import sys

def inp():
    n = int(input())
    sensor = [0, ]
    sensorsum = 0
    for x in range(n):
        st = sys.stdin.readline()
        st = int(st.rstrip())
        sensorsum += st
        sensor.append(sensorsum)
    n_slice = int(input())
    z = ''
    for line in range(n_slice):
        st = sys.stdin.readline()
        s_slice = list(map(int, st.split()[:2]))
        z += str(sensor[s_slice[1]] - sensor[s_slice[0]-1]) + '\n'
    sys.stdout.write(z)
    sys.stdout.flush()
        
inp()