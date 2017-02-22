from random import randint
import math

def limit_val(val, inf, sup):
    val = min(val, sup)
    val = max(val, inf)
    return val

cols = 0
rows = 0

class Wave:
    count     = 3
    walk_rate = 0.001
    def __init__(self):
        self.mean = [0, 0]
        #self.mean = [randint(0, cols), randint(0, rows)]
        self.strength = 1.
    def walk(self):
        self.mean[0] += self.walk_rate * (randint(0, 10) - 5)
        self.mean[0] = limit_val(self.mean[0], -1, cols + 1)

        self.mean[1] += self.walk_rate * (randint(0, 10) - 5)
        self.mean[1] = limit_val(self.mean[1], -1, rows + 1)

        self.strength += self.walk_rate * (randint(0, 10) - 4)
        self.strength = limit_val(self.strength, 0., 1.)
    def value(self):
        # Could be mutable in the future
        return 1.

waves = []
def waves_init(inp_cols, inp_rows):
    global cols, rows
    cols = inp_cols
    rows = inp_rows
    # Initialize waves
    for i in range(0, Wave.count):
        waves.append(Wave())

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def wave_force(pt, w):
    return 225. * w.value() * math.exp(-0.5 * (dist(pt, w.mean)))

def waves_update():
    for w in waves:
        w.walk()

def wave_pressure(f_x, f_y):
    res = []
    for w in waves:
        x = f_x - w.mean[0]
        y = f_y - w.mean[1]
        z = wave_force((f_x, f_y), w)
        length = math.sqrt(x**2 + y**2 + z**2) # Should be wave_force((x, y), w)
        if (length > 0):
            coef = z / length;
            x *= coef
            y *= coef
            z *= coef
            res.append([x, y, z])

    return res
