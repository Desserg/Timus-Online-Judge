import sys
import random
import time

a = [i for i in range(10001)]
b = []
for i in range(100001):
    f = random.randint(0, 9999)
    b.append([random.randint(0, f), random.randint(f, 10000)])


def inp():
    sensorsum = 0
    sensor = []
    for i in range(10001):
        sensorsum += a[i]
        sensor.append(sensorsum)
    z = ''
    for i in range(100001):
        z += str(sensor[b[i][1]] - sensor[b[i][0]-1]) + '\n'
    return z
     
start_time = time.time()
z = inp()
print(z)
print("--- %s seconds ---" % (time.time() - start_time))