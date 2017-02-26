#!/usr/bin/python2

"""
Supposed to be used with websocketd
"""
from time import sleep
from random import randint
import math
import random
import waves

random.seed(68)

cols = 14
rows = 4

def limit_val(val, inf, sup):
    val = min(val, sup)
    val = max(val, inf)
    return val

# Agent description
#alpha_lim = [0., math.pi / 2]
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
        if cols % 2 == 0:
            self.r = abs(x - cols / 2) + 0.5
        else:
            self.r = abs(x - cols / 2)

feathers = []

for i in range(0, cols):
    tmp = []
    for j in range(0, rows):
        tmp.append(Feather(i, j))
    feathers.append(tmp)

def neighbours(col, row):
    res = []
    if (col > 1):
        res.append(feathers[col - 1][row])
    if (row > 1):
        res.append(feathers[col][row - 1])
    if (col < cols - 1):
        res.append(feathers[col + 1][row])
    if (row < rows - 1):
        res.append(feathers[col][row + 1])
    return res

world_update   = waves.waves_update
world_pressure = waves.wave_pressure
world_init     = waves.waves_init

world_init(cols, rows)

while 1:
    out = ""
    for l in feathers:
        for f in l:
            out += str(int(limit_val(f.pressure, 0, 255))) + " "
    print out
    sleep(0.01)

    world_update()

    for l in feathers:
        for f in l:
            f.pressure_prev = f.pressure

    for l in feathers:
        for f in l:
            f.pressure = 0
            for p in world_pressure(f.x, f.y): # list of 3d-vectors
                f.pressure += p[2]
                continue
                #p[0] = 0
                #p[1] = 0
                # If scalar product of the pressure vector and the
                # normal to the feather is negative then this wind
                # flow do not affect this side of the feather
                n = [math.cos(f.beta), math.sin(f.beta), math.cos(f.alpha)]
                s = p[0] * n[0] + p[1] * n[1] + p[2] * n[2]
                if s > 0 and math.cos(f.alpha) != 0:
                    f.pressure += p[2] * math.cos(f.alpha) + p[1] * math.sin(f.alpha) + p[0] * math.sin(f.beta)#s / abs(math.cos(f.alpha))
                    #f.pressure += s / math.sqrt(n[0]** 2 + n[1] ** 2 + n[2] ** 2)


    b = 0.5
    gamma = .01
    for i in range(0, cols):
        for j in range(0, rows):
            weighted_diff = 0.
            #print "My val: " + str(f.pressure)
            for h in neighbours(i, j):
                #print "neigh: " + str(h.pressure)
                weighted_diff += b * (h.pressure - feathers[i][j].pressure)
            alpha = feathers[i][j].alpha

            f = limit_val(feathers[i][j].pressure, 0.01, 1024)
            f_prev = limit_val(feathers[i][j].pressure_prev, 0.01, 1024)

            step = weighted_diff - math.tan(alpha) * (math.log(f) - math.log(f_prev))
            if feathers[i][j].r > 0:
                step /= feathers[i][j].r * f * math.cos(alpha)
            alpha -= gamma * step
            '''
            if (weighted_diff > 0):
                alpha -= gamma * step
            else:
                alpha += gamma * step
            '''
            feathers[i][j].alpha = limit_val(alpha, alpha_lim[0], alpha_lim[1])

            #f.pressure = limit_val(f.pressure, 0, 255)
            #diff = gamma * (weighted_diff - math.tan(alpha) * (1.)) / (1)

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

