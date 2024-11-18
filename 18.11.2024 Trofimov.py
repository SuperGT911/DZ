
#------------ ЗД 3 ------------#
''' удалите эту строку


import turtle as t
#import math
#result = (20*math.sqrt(3))

t.tracer(0,0)

k = 10
t.left(90)
for _ in range(9):
    t.forward(29*k)
    t.right(90)
    t.forward(17*k)
    t.right(90)
t.up()
t.forward(5*k)
t.right(90)
t.forward(1*k)
t.left(90)
t.down()
for _ in range(9):
    t.forward(64*k)
    t.right(90)
    t.forward(48*k)
    t.right(90)
t.up()

''' #удалите эту строку

'''
for x  in range(-20,20):
    for y in range(-10,10):
        t.goto(x*k,y*k)
        t.dot(3)
a=input()'''

#------------ ЗД 4 ------------#
''' #удалите эту строку

import turtle as t
#import math
#result = (20*math.sqrt(3))

t.tracer(0,0)

k = 20
t.left(90)
t.right(45)
for _ in range(7):
    t.forward(5*k)
    t.right(45)
    t.forward(10*k)
    t.right(135)
t.up()

#рисуем точки
for x  in range(0,15):
    for y in range(-1,5):
        t.goto(x*k,y*k)
        t.dot(3)
a=input()

''' #удалите эту строку

#------------ ЗД 5 ------------#
''' #удалите эту строку

import turtle as t
#import math
#result = (20*math.sqrt(3))

t.tracer(0,0)

k = 20
t.left(90)
for _ in range(6):
    t.forward(13*k)
    t.right(120)
t.up()

#рисуем точки
for x  in range(0,13):
    for y in range(-1,15):
        t.goto(x*k,y*k)
        t.dot(3)
a=input()

''' #удалите эту строку

#------------ ЗД 6 ------------#

import turtle as t
#import math
#result = (20*math.sqrt(3))

t.tracer(0,0)

k = 20
t.left(90)
for _ in range(12):
    t.right(60)
    t.forward(1*k)
    t.right(60)
    t.forward(1*k)
    t.right(270)
t.up()

#рисуем точки
for x  in range(-4,6):
    for y in range(-8,2):
        t.goto(x*k,y*k)
        t.dot(3)
a=input()