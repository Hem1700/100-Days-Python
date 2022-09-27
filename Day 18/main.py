import random
import turtle
from turtle import Turtle, Screen

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'wheat', 'LightSeaGreen',
          'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]
timmy = Turtle()
timmy.speed('fastest')
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
#
#
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(i)

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.pensize(5)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))






screen = Screen()
screen.exitonclick()

