import turtle

#print(turtle.colormode())  # 1.0
#exit()
turtle.colormode(255)

def objekt(strana=100, úhel=90):
    for i in range(360 // úhel):
        turtle.forward(strana)
        turtle.left(úhel)

turtle.speed(0)
for i in range(51):
    turtle.pencolor(5*i, 0, 0)
    objekt(úhel=60)
    turtle.left(360 // 51)

turtle.mainloop()
