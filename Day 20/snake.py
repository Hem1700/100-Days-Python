from re import S
from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]


    def createSnake(self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(position)
            self.segments.append(new_turtle)


    def move_turtle(self):
        for seg_number in range( len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_number-1].xcor()
            new_y = self.segments[seg_number-1].ycor() 
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        
        