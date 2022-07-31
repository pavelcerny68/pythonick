import turtle

turtle.colormode(255)

turtle.speed(255)
kroků = 51
pootočení = 360 // kroků
for i in range(kroků):
    turtle.pencolor(5 * i, 0, 0)
    turtle.circle(100)
    turtle.left(pootočení)

turtle.mainloop()
