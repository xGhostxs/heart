import math
from turtle import *
import time


def kalp1(a):
    return 15 * math.sin(a)**3

def kalp2(a):
    return 12 * math.cos(a) - 5 *\
           math.cos(2*a) - 2*\
           math.cos(3*a) - \
           math.cos(4*a)


def kalp3(k):
    return 15 * math.sin(k) ** 3

def kalp4(k):
    return 12 * math.cos(k) - 4 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

tracer(2)
bgcolor("black")
for x in range(800):
    goto(kalp1(x)*15 , kalp2(x)*15)
    for z in range(1):
        color('red')
        hideturtle
        goto(0,0)

start_time = time.time()
for i in range(600):
    if time.time() - start_time > 1:  
        break
    goto(kalp3(i) * 25 , kalp4(i) * 25)



done()  
