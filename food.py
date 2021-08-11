from turtle import Turtle
from random import Random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random = Random()
        self.refresh()
    
    def refresh(self):
        '''Create food and place randomly on the screen'''

        self.x_coordinate = self.random.randint(-280,280)
        self.y_coordinate = self.random.randint(-280,280)
        self.goto(self.x_coordinate, self.y_coordinate)
        self.food_exists = True

    def delete_food(self):
        self.food.reset()
        self.food_exists = False