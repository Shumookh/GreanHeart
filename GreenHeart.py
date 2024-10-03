import math
from turtle import *

def hearta(k):
    return 16 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 6 * math.cos(2 * k) - 3 * math.cos(3 * k) - math.cos(4 * k)

# Set up turtle graphics
speed(100000)
bgcolor('black')
penup()
goto(10, 10)
pendown()
color("#1b5e20")

for i in range(99999):
    goto(hearta(i) * 10, heartb(i) * 10)

done()