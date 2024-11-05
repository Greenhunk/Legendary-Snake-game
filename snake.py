from turtle import Turtle, Screen
screen = Screen()
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
     self.xx = 0
     self.yy = 0
     for _ in range(3):
         self.add_segment(_)

    def add_segment(self, _):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=self.xx, y=self.yy)
        self.xx -= 20
        self.segments.append(new_segment)
    def reset(self):
        for seg in self.segments:
           seg.goto(1000, 1000)
        self.segments.clear()
        self.add_segment(0)
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

       for seg_num in range(len(self.segments) - 1, 0, -1):
          new_x = self.segments[seg_num - 1].xcor()
          new_y = self.segments[seg_num - 1].ycor()
          self.segments[seg_num].goto(new_x, new_y)
       self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
           self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
          self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
          self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
          self.segments[0].setheading(LEFT)