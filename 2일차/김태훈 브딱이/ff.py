import turtle
a=turtle.Pen()
a.color('blue')
a.shape('triangle')
b=turtle.Pen()
b.color('red')
b.shape('circle')

a.forward(200)
b.forward(100)
b.left(90)
b.forward(70)
b.right(90)
b.forward(100)

turtle.exitonclick()
