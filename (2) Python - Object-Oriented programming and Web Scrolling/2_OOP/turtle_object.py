import turtle


# tom = turtle.Turtle()
# tom.circle(100)
#
# print(type(tom))

nonte = turtle.Turtle()
fonte = turtle.Turtle()

nonte.shape("circle")
fonte.shape("square")

nonte.left(30)
nonte.forward(100)
fonte.backward(50)

monte = turtle.Turtle()
monte.setpos(-100, 100)
monte.forward(30)

monte.clear()
nonte.clear()
fonte.clear()

fonte.shape("triangle")
monte.shape("square")

turtle.done()

