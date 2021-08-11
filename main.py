from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=1000, width=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    
    time.sleep(0.1)    
    screen.tracer(0)
    snake.move()
    screen.update()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.point_scored()
        food.refresh()
        snake.increase_size()

    # Detect collision with boundaries
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail 
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:                
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()