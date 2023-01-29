# simple pong game
# by Nibijja

import turtle
import time
import winsound

wn = turtle.getscreen()
wn.tracer(0)
wn.title("Pong by Nibijja")
wn.setup(800, 600)
wn.bgcolor("black")

score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.shape("square")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .66
ball.dy = .5

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0     Player B : 0", align = "center", font  = ("Courier", 24, "normal"))

# functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    time.sleep(1/500)
    wn.update()
    
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border checking
    if ball.ycor() > 290:
        ball.dy *= -1
        ball.sety(ball.ycor() + ball.dy)
        winsound.PlaySound('pong/resource/audio/bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.dy *= -1
        ball.sety(ball.ycor() + ball.dy)
        winsound.PlaySound('pong/resource/audio/bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b), align = "center", font  = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b), align = "center", font  = ("Courier", 24, "normal"))
        

    # bouncing the ball from paddle
    if ball.xcor() > 340 and ball.xcor() < 341 and (ball.ycor()-10 < paddle_b.ycor() + 50 and ball.ycor()+10 > paddle_b.ycor() - 50):
        ball.dx *= -1
        ball.setx(340 + ball.dx)
        winsound.PlaySound('pong/resource/audio/bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() < -340 and ball.xcor() > -341 and (ball.ycor()-10 < paddle_a.ycor() + 50 and ball.ycor()+10 > paddle_a.ycor() - 50):
        ball.dx *= -1
        ball.setx(-340 + ball.dx)
        winsound.PlaySound('pong/resource/audio/bounce.wav', winsound.SND_ASYNC)