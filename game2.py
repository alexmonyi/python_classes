import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Randomized Pong Game")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)

# Paddle (bat)
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -180)

# Ball
ball = turtle.Turtle()
ball.speed(1)  # Reduced speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-0.1, 0.1])
ball.dy = random.choice([-0.1, 0.1])

# Score variables
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Function to move the paddle to the left
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -290:
        x = -290
    paddle.setx(x)

# Function to move the paddle to the right
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 290:
        x = 290
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Paddle collision
    if (
        ball.xcor() < paddle.xcor() + 50
        and ball.xcor() > paddle.xcor() - 50
        and ball.ycor() < paddle.ycor() + 10
        and ball.ycor() > paddle.ycor() - 10
    ):
        ball.dy *= -1
        score += 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check if ball hits the left or right wall
    if ball.xcor() < -290 or ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx = random.choice([-0.1, 0.1])
        ball.dy = random.choice([-0.1, 0.1])

# Close the window when clicked
turtle.done()
