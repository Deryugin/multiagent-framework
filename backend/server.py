#!/usr/bin/python2

"""
A simple echo server
"""
from time import sleep
from random import randint

host = ''
port = 50000
backlog = 5
size = 1024

p = []

cols = 15
rows = 4

for i in range(0, rows):
    p.append([])
    for j in range(0, cols):
        p[i].append(0.0 + randint(0, 255))

r = 0

while 1:
    out = ""
    for j in range(0, cols):
        for i in range(0, rows):
           out += str(int(p[i][j])) + " "
    #      print p[i][j]
    print out
    #continue;
    sleep(0.01)

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


