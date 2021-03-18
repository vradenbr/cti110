import turtle
window = turtle.Screen()
window.title("Triangle & Square")

square = turtle.Turtle()
square.color("blue")

for i in [0,1,2,3]:
    square.forward(75)
    square.left(90)

triangle = turtle.Turtle()

triangle.penup()
triangle.forward(160)
triangle.pendown()

triangle.color("red")
for i in [0,1,2]:
    triangle.forward(85)
    triangle.left(120)



