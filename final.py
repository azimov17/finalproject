import turtle

wn=turtle.Screen()
wn.title("Pong by Azimov and Suborov")
wn.bgcolor("greenyellow")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_azimov = 0
score_suborov = 0

#Paddle Azimov
paddle_azimov=turtle.Turtle()
paddle_azimov.speed(0)
paddle_azimov.shape("square")
paddle_azimov.color("red")
paddle_azimov.shapesize(stretch_wid=10, stretch_len=1)
paddle_azimov.penup()
paddle_azimov.goto(-650, 0)



#Paddle Suborov
paddle_suborov=turtle.Turtle()
paddle_suborov.speed(0)
paddle_suborov.shape("square")
paddle_suborov.color("red")
paddle_suborov.shapesize(stretch_wid=10, stretch_len=1)
paddle_suborov.penup()
paddle_suborov.goto(650, 0)

#Ball
ball=turtle.Turtle()
ball.speed(18)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx=2
ball.dy=-2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Azimov: 0    Suborov: 0 ", align="center", font=("Arial", 24, "normal"))

#Function
def paddle_azimov_up():
    y=paddle_azimov.ycor()
    y+=20
    paddle_azimov.sety(y)

def paddle_azimov_down():
    y=paddle_azimov.ycor()
    y-=20
    paddle_azimov.sety(y)


def paddle_suborov_up():
    y=paddle_suborov.ycor()
    y+=20
    paddle_suborov.sety(y)

def paddle_suborov_down():
    y=paddle_suborov.ycor()
    y-=20
    paddle_suborov.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_azimov_up, "w")
wn.onkeypress(paddle_azimov_down, "s")
wn.onkeypress(paddle_suborov_up, "Up")
wn.onkeypress(paddle_suborov_down, "Down")




#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*= -1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*= -1

    if ball.xcor() >690:
        ball.goto(0, 0)
        ball.dx *= -1
        score_azimov += 1
        pen.clear()
        pen.write("Azimov:{}    Suborov:{}".format(score_azimov,score_suborov), align ="center", font=("Arial",24,"normal"))

    if ball.xcor() < -690:
        ball.goto(0, 0)
        ball.dx *= -1
        score_suborov += 1
        pen.clear()
        pen.write("Azimov:{}   Suborov:{}".format(score_azimov,score_suborov),align ="center",font=("Arial",24,"normal"))
    
    #Paddle and ball collisions
    if (ball.xcor() > 640 and ball.xcor() < 650) and (ball.ycor() < paddle_suborov.ycor() + 100 and ball.ycor() > paddle_suborov.ycor() -100):
        ball.setx(640)
        ball.dx *= -1

    if (ball.xcor() < -640 and ball.xcor() > -650) and (ball.ycor() < paddle_azimov.ycor() + 100 and ball.ycor() > paddle_azimov.ycor() -100):
        ball.setx(-640)
        ball.dx *= -1