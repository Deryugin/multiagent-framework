#!/usr/bin/python2

"""
Supposed to be used with websocketd
"""
from time import sleep
from random import randint
import math

cols = 15
rows = 4

def limit_val(val, inf, sup):
    val = min(val, sup)
    val = max(val, inf)
    return val

class Wave:
    count     = 3
    walk_rate = 0.01
    def __init__(self):
        self.mean = [randint(0, rows), randint(0, cols)]
        self.strength = 1.
    def walk(self):
        self.mean[0] += self.walk_rate * (randint(0, 10) - 5)
        self.mean[0] = limit_val(self.mean[0], -1, rows + 1)

        self.mean[1] += self.walk_rate * (randint(0, 10) - 5)
        self.mean[1] = limit_val(self.mean[1], -1, cols + 1)

        self.strength += self.walk_rate * (randint(0, 10) - 4)
        self.strength = limit_val(self.strength, 0., 1.)
    def value(self):
        # Could be mutable in future
        return 1.

class Feather:
    alpha    = 0.
    beta     = 0.
    pressure = 0.
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Initialize waves
waves = []
for i in range(0, Wave.count):
    waves.append(Wave())

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def wave_pressure(pt, w):
    return 225. * w.value() * math.exp(-0.5 * (dist(pt, w.mean)))

feathers = []

for j in range(0, cols):
    for i in range(0, rows):
        feathers.append(Feather(i, j))

r = 0

while 1:
    out = ""
    for f in feathers:
        out += str(int(f.pressure)) + " "
    print out
    sleep(0.01)

    for w in waves:
        w.walk()

    for f in feathers:
            p = 0
            for w in waves:
                p += wave_pressure((f.x, f.y), w)
                limit_val(p, 0, 255)

            p *= math.cos(f.alpha)
            f.pressure = p
'''
    b = 0.005

    for i in range(0, rows):
        for j in range(0, cols):
            diff = 0;
            if (i > 0):
                diff += b * (p[i - 1][j] - p[i][j])
            if (j > 0):
                diff += b * (p[i][j - 1] - p[i][j])
            if (i < rows - 1):
                diff += b * (p[i + 1][j] - p[i][j])
            if (j < cols - 1):
                diff += b * (p[i][j + 1] - p[i][j])
            p[i][j] += diff
            if (p[i][j] > 255):
                #print str(diff) + " " + str(p[i][j])
                p[i][j] = 255;
            if (p[i][j] < 0):
                #print str(diff) + " " + str(p[i][j])
                p[i][j] = 0;

    r += 1
    if (r % int(5. / b) == 0):
        for i in range(0, rows):
            for j in range(0, cols):
                p[i][j] += randint(0, 512) - 255
                if (p[i][j] > 255):
                    p[i][j] = 255;
                if (p[i][j] < 0):
                    p[i][j] = 0;
'''

