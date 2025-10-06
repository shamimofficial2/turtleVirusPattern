import turtle as t

screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)

t.title("Turtle Virus Pattern")
t.color("white")
t.bgcolor("black")
t.speed(0)
t.pensize(2)
t.hideturtle()
t.penup()
t.goto(0,-100)
t.pendown()

x = 0 
i = 0
while i < 210:
    t.forward(x)
    t.left(i)
    x += 2 
    i += 1

t.exitonclick()
