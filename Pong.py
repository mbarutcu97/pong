# Importeren van Turtle library, pre-installed graphics library van Python
import turtle
 
 
# Canvas creëren
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
 
 
# Linker vierkant creëren
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
 
# Rechter vierkant creëren
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
 
# Cirkel bal creëren
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5
 
 
# Score variabelen opzetten
left_player = 0
right_player = 0
 
 
# Score tonen
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))
 
 
# Functies om vierkanten verticaal te bewegen
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
 
speed = 10
while True:
    sc.update()
 
    # Terwijl de loop bezig is, zal de X en Y positie van het balletje altijd veranderd worden met DX of DY, 
    # dit is de hoeveelheid waarmee de xcoordinaat of ycoordinaat van het balletje zou veranderen) als het balletje één stap vooruit zou zetten in zijn huidige richting
    
    hit_ball.setx(hit_ball.xcor()+speed)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
 

    # Als het balletje onder of boven grens van het canvas bereikt, zal het terug naar boven / beneden gekaatst worden
    # Binnen Turtle graphics library worden de coordinaten geprogrammeerd relatief aan het midden van het canvas
    # sety(280) betekent dus dat de positie van het balletje 280 boven het midden van het canvas wordt geplaatst 
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
 
    #  Als het balletje door een speler gemist wordt, dan krijgt een tegenstander een punt
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
 
    # Als de positie van het balletje rand van het vierkantje aanraakt dan zal het teruggekaatst worden
    if (hit_ball.xcor() > 360 and hit_ball.xcor() == 380) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40): 
        hit_ball.setx(360)
        speed*=-1
        
    if (hit_ball.xcor() < -360 and hit_ball.xcor() == -380) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
        hit_ball.setx(-360)
        speed*=-1

   # AI speler
   # Volg het balletje (abs = absolute number) als  balletje omhoog / omlaag gaat en verschil in hoogte is hoger dan 10 (zodat het niet omhoog/omlaag gaat als balletje laag / hoog genoeg is)
    if left_pad.ycor() < hit_ball.ycor() and abs(left_pad.ycor() -  hit_ball.ycor()) > 10:
        paddleaup()

    elif left_pad.ycor() >  hit_ball.ycor() and abs(left_pad.ycor() -  hit_ball.ycor()) > 10:
       paddleadown()
