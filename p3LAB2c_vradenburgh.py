import turtle
window = turtle.Screen()
window.title("Snowflakes")

for i in range(12):
    for i in range(9):
        turtle.left(360 / 9)
        turtle.forward(100)
    turtle.left(30)

for i in range(12):
    for i in range(3):
        turtle.left(360 / 3)
        turtle.forward(350)
    turtle.left(30)
