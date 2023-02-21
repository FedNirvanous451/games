from turtle import *
from random import choice, randint

#создаем окно
window = Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')
window.tracer(2)

#создаем игрвое поле
border = Turtle()
border.speed(15)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

#создаем центральную линию
border.goto(0, 300)
border.color('white')
border.right(90)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

#создаем ракетки
rocket_one = Turtle()
rocket_one.color('orange')
rocket_one.shape('square')
rocket_one.shapesize(5, 1)
rocket_one.up()
rocket_one.goto(-470, 0)

rocket_two = Turtle()
rocket_two.color('orange')
rocket_two.shape('square')
rocket_two.shapesize(5, 1)
rocket_two.up()
rocket_two.goto(470, 0)

FONT = ('Arial', 50)
score_one = 0
table_one = Turtle(visible=False)
table_one.color('white')
table_one.penup()
table_one.setposition(-200, 300)
table_one.write(score_one, font=FONT)

score_two = 0
table_two = Turtle(visible=False)
table_two.color('white')
table_two.penup()
table_two.setposition(200, 300)
table_two.write(score_two, font=FONT)

def move_up_one():
    y = rocket_one.ycor() + 20
    if y >= 250:
        y = 250
    rocket_one.sety(y)

def move_down_one():
    y = rocket_one.ycor() - 20
    if y <= -250:
        y = -250
    rocket_one.sety(y)




def move_up_two():
    y = rocket_two.ycor() + 20
    if y >= 250:
        y = 250
    rocket_two.sety(y)

def move_down_two():
    y = rocket_two.ycor() - 20
    if y <= -250:
        y = -250
    rocket_two.sety(y)


ball = Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('red')
ball.dx = 0.5
ball.dy = -0.5
ball.penup()

window.listen()
window.onkeypress(move_up_one, 'w')
window.onkeypress(move_down_one, 's')
window.onkeypress(move_up_two, 'Up')
window.onkeypress(move_down_two, 'Down')

while True:
    window.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() <= -490:
        score_two += 1
        table_two.clear()
        table_two.write(score_two, font=FONT)
        ball.goto(0,randint(-150, 150))
        ball.dx = choice([2, 1, 0.5,-1, -2, -0.5]) 
        ball.dy = choice([2, 1, 0.5,-1, -2, -0.5]) 

    if ball.xcor() >= 490:
        score_one += 1
        table_one.clear()
        table_one.write(score_one, font=FONT)
        ball.goto(0,randint(-150, 150))
        ball.dx = choice([2, 1, 0.5,-1, -2, -0.5]) 
        ball.dy = choice([2, 1, 0.5,-1, -2, -0.5]) 

    if ball.ycor() >= rocket_two.ycor() - 50 and ball.ycor() <= rocket_two.ycor() + 50 \
     and ball.xcor() >= rocket_two.xcor() - 5 and ball.xcor() <= rocket_two.xcor() + 5:
        ball.dx = -ball.dx


    if ball.ycor() >= rocket_one.ycor() - 50 and ball.ycor() <= rocket_one.ycor() + 50 \
     and ball.xcor() >= rocket_one.xcor() - 5 and ball.xcor() <= rocket_one.xcor() + 5:
        ball.dx = -ball.dx

window.mainloop()
