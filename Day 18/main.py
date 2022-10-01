import random
import turtle
from turtle import Turtle, Screen
import colorgram


colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'wheat', 'LightSeaGreen',
          'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]
timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    timmy.color(random_color())
    draw_shape(i)

for _ in range(200):
    timmy.color(random_color())
    timmy.pensize(5)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

def draw_spirogragh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)



draw_spirogragh(5)












screen = Screen()
screen.exitonclick()

