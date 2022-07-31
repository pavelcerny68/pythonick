import turtle

def objekt(strana=100, úhel=90):
    for i in range(360 // úhel):
        turtle.forward(strana)
        turtle.left(úhel)

turtle.speed(0)
for i in range(12):
    objekt(úhel=120)
    turtle.left(30)

turtle.mainloop()
