from turtle import Turtle

MOVE_DISTANCE = 15
INITIAL_SNAKE_SIZE = 3
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        '''Create a snake'''
    
        for i in range(INITIAL_SNAKE_SIZE):
            x_coordinate = -MOVE_DISTANCE*i
            y_coordinate = 0

            self.add_segment((x_coordinate, y_coordinate))

    def move(self):
        '''Move a snake forward'''

        # set position of the back segement to the one immediately ahead
        for seg_num in range(len(self.snake) - 1, 0, -1):  #2, 1
            position = self.snake[seg_num - 1].position()
            self.snake[seg_num].goto(position)
            
        self.head.forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_size(self):
        '''Increase snake size'''

        position = self.snake[-1].position()
        self.add_segment(position)
        
    def add_segment(self, position):
        segement = Turtle()
        segement.shapesize(stretch_len=0.7, stretch_wid=0.7)
        segement.penup()
        segement.goto(position)
        segement.color("white")
        segement.shape("square")
        segement.speed(1)
        self.snake.append(segement)
