from turtle import *
import time
import random
from random import randint

# creating the screen
screen = Screen()
screen.bgcolor('light blue')
screen.title('Turtle game')
screen.setup(width = 600, height = 600) #
screen.tracer(0)

# the title
title =Turtle()
title.color('Green')
title.up()
title.goto(0,230)
title.hideturtle()
title.write("Eat the Green, stay away from Red",align='center',font=('Courier',15,'normal'))

# pen for writing score
pen =Turtle()
pen.color('black')
pen.up()
pen.goto(0,260)
pen.hideturtle()
pen.write("Score: 0",align='center',font=('Courier',24,'normal'))

# some initializations
score = 0
num_haz = 2
haz_list = []
food_list = []

for i in range(num_haz):
    # hazzard section
    haz_list.append(Turtle())
    haz_list[i].speed(0)
    haz_list[i].shape('circle')
    haz_list[i].color('red')
    haz_list[i].penup()
    haz_list[i].goto(150,-280)
    haz_list[i].directionVertical = "stable"
    haz_list[i].directionHorizontal = "stable"
    haz_list[i].vertical_step = random.randint(0,250)
    haz_list[i].horizaontal_step = random.randint(0,250)

for i in range(num_haz):
    # food section
    food_list.append(Turtle())
    food_list[i].speed(0)
    food_list[i].shape('circle')
    food_list[i].color('green')
    food_list[i].penup()
    food_list[i].goto(150,-280)
    food_list[i].directionVertical = "stable"
    food_list[i].directionHorizontal = "stable"
    food_list[i].vertical_step = random.randint(0,250)
    food_list[i].horizaontal_step = random.randint(0,250)

# head section
head = Turtle()
head.speed(10)
head.shape('turtle')
head.color('yellow')
head.penup()
head.lastX = 0
head.goto(head.lastX,-280)
head.directionVertical = "stable"
head.directionHorizontal = "stable"
head.vertical_step = 100
head.horizaontal_step = 150


def getRands():
    direction= "left"
    if random.randint(10, 100)> 45: direction = "right"
    return direction

# some listeners
def jump():
    if head.ycor()==-280:
        head.directionVertical = "up"
        head.sety(head.ycor() + 20)

def go_left():
    head.lastX = head.xcor()
    head.directionHorizontal = "left"

def go_right():
    head.lastX = head.xcor()
    head.directionHorizontal = "right"

# move functions
def moveVertical(turtle, always=False):
    if turtle.directionVertical == "stable":
        if always:
            turtle.directionVertical = "up"
            turtle.sety(turtle.ycor()+3)


    if turtle.directionVertical == "up":
        if turtle.ycor() > -280:
            if turtle.ycor() < -280+turtle.vertical_step:
                turtle.sety(turtle.ycor() + 3)
            else:
                turtle.directionVertical = "down"

    elif turtle.directionVertical == "down":
        if turtle.ycor() > -280:
            turtle.sety(turtle.ycor()-3)
        else:
            turtle.directionVertical = "stable"
            turtle.sety(-280)

def moveHorizontal(turtle, always=False):
    if turtle.directionHorizontal == "stable":
        if always:
            turtle.directionHorizontal = getRands()
            turtle.lastX = turtle.xcor()
    if (turtle.xcor() < -280 or turtle.xcor() > 280):
        turtle.setx(turtle.xcor()*-1)
    if turtle.directionHorizontal == "left":

        if turtle.xcor() > turtle.lastX - turtle.horizaontal_step:
            turtle.setx(turtle.xcor() - 3)
        else:
            turtle.directionHorizontal = "stable"
            turtle.lastX = turtle.xcor()
    if turtle.directionHorizontal == "right":
        if turtle.xcor() < turtle.lastX + turtle.horizaontal_step:
            turtle.setx(turtle.xcor() + 3)
        else:
            turtle.directionHorizontal = "stable"
            turtle.lastX = turtle.xcor()

screen.listen()
screen.onkeypress(jump,'Up')
screen.onkeypress(jump,'Down')
screen.onkeypress(go_left,'Left')
screen.onkeypress(go_right,'Right')

gameover = False

while True:

    if gameover:
        time.sleep(5)
        break

    screen.update()
    moveHorizontal(head)
    moveVertical(head)
    for haz in haz_list:
        moveHorizontal(haz, True)
        moveVertical(haz, True)
        if haz.distance(head) <20.0:
            gameover = True
            pen.goto(0,0)
            pen.color("red")
            pen.write(f"Game Over", align='center', font=('Courier', 26, 'normal'))

    for food in food_list:
        moveHorizontal(food, True)
        moveVertical(food, True)
        if food.distance(head)<20.0:
            food.goto(150, -280)
            score += 1
            pen.clear()
            pen.write(f"Score: {score}", align='center', font=('Courier', 24, 'normal'))
    time.sleep(0.01)