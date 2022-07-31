import turtle

turtle.speed(255)


def objekt(strana=100, úhel=90):
    for i in range(360 // úhel):
        turtle.forward(strana)
        turtle.left(úhel)


for i in range(30):
    objekt(úhel=120)
    turtle.left(5)

turtle.mainloop()
