# !/usr/bin/python3.9
# coding=utf-8

import turtle
from time import sleep

# zavedení dvou nezávislých želv
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# první želva
t1.color("red", "yellow")
t1.begin_fill()
t1.circle(100)
t1.end_fill()

# druhá želva
t2.left(60)
t2.color("blue", "violet")
t2.begin_fill()
t2.circle(100)
t2.end_fill()

# ukázka nezávislosti kreseb
sleep(3)
t2.clear()
sleep(3)
t1.clear()

# čekací smyčka
turtle.done()
