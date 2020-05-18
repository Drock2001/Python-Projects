import turtle
turtle.bgcolor("black")
turtle.pensize(2)

turtle.speed(1)
turtle.color("red","blue")
turtle.begin_fill()


for i in range(10):
	turtle.right(144)
	turtle.forward(10)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

