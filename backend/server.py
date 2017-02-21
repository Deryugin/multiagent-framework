#!/usr/bin/python2

"""
Supposed to be used with websocketd
"""
from time import sleep
from random import randint
import math

import waves

cols = 15
rows = 4

def limit_val(val, inf, sup):
    val = min(val, sup)
    val = max(val, inf)
    return val

# Agent description
class Feather:
    alpha    = 0.
    beta     = 0.
    pressure = 0.
    def __init__(self, x, y):
        self.x = x
        self.y = y

feathers = []

for j in range(0, cols):
    for i in range(0, rows):
        feathers.append(Feather(i, j))

world_update   = waves.waves_update
world_pressure = waves.wave_pressure
world_init     = waves.waves_init

world_init(cols, rows)

while 1:
    out = ""
    for f in feathers:
        out += str(int(f.pressure)) + " "
    print out
    sleep(0.01)

    world_update()

    for f in feathers:
        p = world_pressure(f.x, f.y)
        f.pressure = limit_val(p * math.cos(f.alpha), 0, 255)
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

