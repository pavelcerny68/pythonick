import turtle

turtle.colormode(255)

turtle.speed(255)
kroků = 255
pootočení = 360 // kroků
for i in range(kroků):
    turtle.pencolor(i, 0, 0)
    turtle.circle(i)
    turtle.left(pootočení)

turtle.mainloop()
