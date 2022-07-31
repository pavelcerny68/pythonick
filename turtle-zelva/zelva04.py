import turtle

def objekt(strana=100, úhel=90):
    for i in range(360 // úhel):
        turtle.forward(strana)
        turtle.left(úhel)

BARVY = 'red', 'green', 'blue'

turtle.speed(0)
for i in range(30):
    turtle.color(BARVY[i % 3])
    objekt(úhel=60)
    turtle.left(12)

turtle.mainloop()
