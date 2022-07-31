import turtle

def objekt(strana=50, úhel=90):
    for i in range(21):
        turtle.forward(strana)
        turtle.left(úhel)

BARVY = 'red', 'green', 'blue'

turtle.speed(0)
for i in range(12):
    turtle.color(BARVY[i % 3])
    objekt(úhel=50)
    turtle.left(60)

turtle.mainloop()
