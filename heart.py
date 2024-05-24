import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(10000000000)
bgcolor("black")
color("red")
begin_fill()

for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)

end_fill()
done()