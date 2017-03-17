#!/usr/bin/python2

from time import sleep
from random import randint
import math
import random
import sys

import matplotlib.pyplot as plt
import fileinput

res = []
#for i in sys.argv[1:]:
#    res.append(float(i))

for line in fileinput.input():
    for w in line.split():
        res.append(float(w))    

plt.plot(res)

plt.show()
