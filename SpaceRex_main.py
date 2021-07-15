import turtle
import os
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SpaceRex")
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-725,-325)
border_pen.pensize(3)
border_pen.pendown()
for i in range (2):
    border_pen.forward(1450)
    border_pen.left(90)
    border_pen.forward(700)
    border_pen.left(90)
    


border_pen.hideturtle()



turtle.register_shape("enemy_1.gif")
turtle.register_shape("asteroid3_60.gif")
turtle.register_shape("asteroid2_40.gif")
turtle.register_shape("asteroid1_50.gif")


#SCORE
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-640,-350)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))
score_pen.hideturtle()

life = 5

life_pen = turtle.Turtle()
life_pen.speed(0)
life_pen.color("white")
life_pen.penup()
life_pen.setposition(560,-350)
lifestring = "Lives left: %s" %life
life_pen.write(lifestring, False, align = "left",font=("Arial",14,"normal"))
life_pen.hideturtle()

title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("white")
title_pen.penup()
title_pen.setposition(-100,-370)
titlestring = "SPACEREX" 
title_pen.write(titlestring, False, align = "left",font=("Arial",25,"normal"))
title_pen.hideturtle()

#PLAYER

#player ship
player = turtle.Turtle()
player.color("blue")
player.shapesize(2,4)
player.penup()
player.speed(0)

playerspeed = 15
player_rotate_angle = 5

#PLAYER BULLET

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.speed(0)
bullet.setheading(player.heading())
bullet.hideturtle()

bulletstate = 'Ready'
bulletspeed = 25


#player movements

def move_forward():
    player.forward(playerspeed)

def move_backward():
    player.backward(playerspeed)

def rotate_left():
    player.left(player_rotate_angle)

def rotate_right():
    player.right(player_rotate_angle)

def fire_space():
    global bulletstate
    if bulletstate == 'Ready':
        bullet.setpos(player.xcor(),player.ycor())
        bullet.setheading(player.heading())
        bullet.showturtle()
        bulletstate = 'Fired'

def iscollision(t1,t2):
    dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if dist < 25:
        return True
    else:
        return False

def iscollisiona(t1,t2):
    dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if dist < 30:
        return True
    else:
        return False


#keyboard binds
turtle.listen()
turtle.onkey(move_forward,"Up")
turtle.onkey(move_backward,"Down")
turtle.onkeypress(rotate_left,"Left")
turtle.onkeypress(rotate_right,"Right")
turtle.onkey(fire_space,"space")
             
#ENEMY

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy_1.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-700,700),370)
    enemy.setheading(random.randint(210,330))

enemyspeed = 20


#ASTERIODS
number_of_asteriods = 7

asteriods = []

for i in range(number_of_asteriods):
    asteriods.append(turtle.Turtle())

counter_2 = 0
for asteriod in asteriods:
    asteriod.color("white")
    if counter_2 == 0:
        asteriod.shape("asteroid3_60.gif")
    elif counter_2 == 1:
        asteriod.shape("asteroid2_40.gif")
    else:
        asteriod.shape("asteroid1_50.gif")

    counter_2 += 1
    
    if counter_2 > 3:
        counter_2 = 0
        
    asteriod.penup()
    asteriod.speed(0)
    asteriod.setposition(random.randint(-700,700),random.randint(-280,360))
    asteriod.setheading(180)
    size = random.randint(10,30)/100
    asteriod.shapesize(size,size)

asteriod_speed_list = []

for i in range(number_of_asteriods):
    asteriod_speed_list.append(random.randint(3,10))
    


while True:

    #move enemies
    for enemy in enemies:
        enemy.forward(enemyspeed)
        angle = 0
        angle = math.degrees(math.atan(math.fabs((player.ycor() - enemy.ycor())/(player.xcor()-enemy.xcor()))))
        diff_x = player.xcor()-enemy.xcor()
        diff_y = player.ycor() - enemy.ycor()
        if diff_y > 0 and diff_x > 0:
            angle = angle
        elif diff_y < 0 and diff_x > 0:
            angle = 360 - angle
        elif diff_y >0 and diff_x < 0 :
            angle = 180 - angle
        else:
            angle = 180 + angle
        enemy.setheading(angle)

        if iscollision(enemy,player):
            enemy.setposition(random.randint(-700,700),370)
            enemy.setheading(random.randint(210,330))
            player.hideturtle()
            player.setposition(0,-400)
            player.setheading(90)
            player.showturtle()
            score -= 100
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))
            life -= 1
            lifestring = "Lives left: %s" %life
            life_pen.clear()
            life_pen.write(lifestring, False, align = "left",font=("Arial",14,"normal"))
            


        if iscollision(enemy,bullet):
            enemy.setposition(random.randint(-700,700),370)
            enemy.setheading(random.randint(210,330))
            bullet.hideturtle()
            bulletstate = 'Ready'
            bullet.setposition (1000,1000)
            score += 100
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))


        if enemy.xcor() < -700 or enemy.xcor() > 700 or enemy.ycor() > 371 or enemy.ycor() < -320:
            enemy.left(random.randint(90,270))

    if bullet.xcor() < -700 or bullet.xcor() > 700 or bullet.ycor() > 371 or bullet.ycor() < -320:
        bulletstate = 'Ready'
        bullet.setposition(1000,1000)


    if bulletstate == 'Fired':
        bullet.fd(bulletspeed)

    counter_1 = 0
    for asteriod in asteriods:
        asteriod.forward(asteriod_speed_list[counter_1])

        if iscollisiona(asteriod,bullet):
            asteriod.hideturtle()
            asteriod.setposition(700,random.randint(-300,350))
            asteriod.setheading(180)
            asteriod.showturtle()
            bullet.hideturtle()
            bulletstate = 'Ready'
            bullet.setposition (1000,1000)
            score += 20
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))

        if iscollisiona(asteriod,player):
            asteriod.hideturtle()
            asteriod.setposition(700,random.randint(-280,370))
            asteriod.setheading(180)
            asteriod.showturtle()
            player.hideturtle()
            player.setposition(0,-400)
            player.setheading(90)
            player.showturtle()
            score -= 100
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))
            life -= 1
            lifestring = "Lives left: %s" %life
            life_pen.clear()
            life_pen.write(lifestring, False, align = "left",font=("Arial",14,"normal"))
            


        for enemy in enemies:
            if iscollisiona(asteriod,enemy):
                enemy.setposition(random.randint(-700,700),370)
                enemy.setheading(random.randint(210,330))
                asteriod.hideturtle()
                asteriod.setposition(700,random.randint(-280,370))
                asteriod.setheading(180)
                asteriod.showturtle()
                score += 120
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align = "left",font=("Arial",14,"normal"))

        if asteriod.xcor() < (-700):
            asteriod.setposition(700,random.randint(-300,370))

       
        counter_1 += 1

        if life == 0:
            for enemy in enemies:
                enemy.hideturtle()
            for asteriod in asteriods:
                asteriod.hideturtle()
            player.hideturtle()
            bullet.hideturtle()

            last_pen = turtle.Turtle()
            last_pen.speed(0)
            last_pen.color("white")
            last_pen.penup()
            score_pen.setposition(-125,-100)
            last_pen.setposition(-200,0)
            laststring = "GAME OVER" 
            last_pen.write(laststring, False, align = "left",font=("Arial",40,"normal")  )
            score_pen.write(scorestring, False, align = "left",font=("Arial",30,"normal"))
            last_pen.hideturtle()
            turtle.exitonclick()
	    





