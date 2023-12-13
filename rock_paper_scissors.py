import turtle
import winsound


#Screen

wn = turtle.Screen()
wn.title("Pong game to have lots of fun :)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))

#Instructions

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(300,-260)
pen2.write("↑ Key: Go Up\n↓ Key: Go Down", align="center", font=("Courier",12, "normal"))

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(-300,-260)
pen3.write('"W" Key: Go Up\n"S" Key: Go Down', align="center", font=("Courier",12, "normal"))



#Move up left rectangle

def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

#Move down left rectangle

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

#Move up right rectangle

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

#Move down right rectangle

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)



#Calling motion functions

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main game loop

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Ball bounces at borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))

    #Limits for paddles

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)




    #Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
