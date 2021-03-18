import turtle
window = turtle.Screen()
window.title("Initials")

first = turtle.Turtle()
first.color("green")
first.pensize(5)

last = turtle.Turtle()
last.color("magenta")
last.pensize(5)

first.left(90)
first.forward(100)
first.right(90)
count = 19
while count > 0:
    first.forward(5)
    first.right(10)
    count = count - 1
first.left(140)
first.forward(56)

last.penup()
last.forward(100)
last.left(90)
last.forward(100)
last.pendown()
last.right(160)
last.forward(105)
last.left(145)
last.forward(105)
