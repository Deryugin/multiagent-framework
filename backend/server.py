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
alpha_lim = [0., math.pi / 4]
beta_lim = [-math.pi / 2, math.pi / 2]

class Feather:
    alpha    = 0.
    beta     = 0.
    pressure = 0.
    pressure_prev = 0.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __getitem__(self, a): #XXX
        return self

feathers = []

for j in range(0, cols):
    for i in range(0, rows):
        feathers.append(Feather(i, j))

def neighbours(row, col):
    res = []

    if (row > 1):
        res.append(feathers[row - 1][col])
    if (col > 1):
        res.append(feathers[row][col - 1])
    if (row < rows - 1):
        res.append(feathers[row + 1][col])
    if (col < cols - 1):
        res.append(feathers[row][col + 1])

    return res

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
        f.pressure = 0
        for p in world_pressure(f.x, f.y): # list of 3d-vectors
            # If scalar product of the pressure vector and the
            # normal to the feather is negative then this wind
            # flow do not affect this side of the feather
            n = [math.cos(f.beta), math.sin(f.beta), math.cos(f.alpha)]
            s = p[0] * n[0] + p[1] * n[1] + p[2] * n[2]
            if s > 0 and math.cos(f.alpha) != 0:
                f.pressure += s / abs(math.cos(f.alpha))
                #f.pressure += s / math.sqrt(n[0]** 2 + n[1] ** 2 + n[2] ** 2)

        f.pressure = limit_val(f.pressure, 0, 255)

    b = 0.005
    gamma = 0.1
    for i in range(0, rows):
        for j in range(0, cols):
            weighted_diff = 0.
            for h in neighbours(i, j):
                weighted_diff += b * (h.pressure - feathers[i][j].pressure)
            alpha = feathers[i][j].alpha

            diff = gamma * (weighted_diff - math.tan(alpha) * (1.)) / (1)

#    for i in range(0, rows):
#        for j in range(0, cols):
#            feathers[i][j].pressure_prev = feathers[i][j].pressure

'''
    for i in range(0, rows):
        for j in range(0, cols):
            diff = 0;
            if (i > 0):
                diff += b * (feathers[i - 1][j] - p[i][j])
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

